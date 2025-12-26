"""
PostgreSQL and SQLite database module for NHS Unified Nursing Validator.

Provides database connection pooling, schema management, and ORM operations
for chat history, users, sessions, and audit logs.
"""

import os
import json
import logging
import sqlite3
import threading
from datetime import datetime, date
from typing import Optional, List, Dict, Any, Generator, Tuple
from contextlib import contextmanager

try:
    import psycopg2
    from psycopg2 import pool, sql
    from psycopg2.extras import RealDictCursor, execute_values
    PSYCOPG2_AVAILABLE = True
except ImportError:
    PSYCOPG2_AVAILABLE = False
    # Define dummy classes to prevent NameError
    pool = None  
    RealDictCursor = None

from core.settings import settings

logger = logging.getLogger(__name__)

# Connection pool for Postgres (initialized on first use)
_pg_pool = None

# Thread-local storage for SQLite connections (since they can't be shared across threads easily)
_local_sqlite = threading.local()

def _get_sqlite_conn():
    """Get thread-local SQLite connection."""
    if not hasattr(_local_sqlite, "conn"):
        _local_sqlite.conn = sqlite3.connect(
            settings.SQLITE_DB_PATH, 
            check_same_thread=False,
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        _local_sqlite.conn.row_factory = sqlite3.Row
    return _local_sqlite.conn

def init_connection_pool():
    """Initialize the PostgreSQL connection pool if needed."""
    global _pg_pool
    if settings.DB_TYPE == "postgres":
        if not PSYCOPG2_AVAILABLE:
            raise ImportError("psycopg2 is required for 'postgres' DB_TYPE")
            
        if _pg_pool is None:
            try:
                _pg_pool = psycopg2.pool.SimpleConnectionPool(
                    settings.DB_POOL_MIN,
                    settings.DB_POOL_MAX,
                    host=settings.DB_HOST,
                    port=settings.DB_PORT,
                    database=settings.DB_NAME,
                    user=settings.DB_USER,
                    password=settings.DB_PASSWORD,
                    connect_timeout=5,
                )
                logger.info("PostgreSQL connection pool initialized successfully")
            except Exception as e:
                from core.safe_logging import log_exception_safe
                log_exception_safe(logger, "Failed to initialize PG pooling", e)
                raise

@contextmanager
def get_connection():
    """Context manager for database connections (Postgres or SQLite)."""
    if settings.DB_TYPE == "sqlite":
        conn = _get_sqlite_conn()
        try:
            yield conn
            conn.commit()
        except Exception as e:
            conn.rollback()
            from core.safe_logging import log_exception_safe
            log_exception_safe(logger, "SQLite DB error", e)
            raise
    else:
        # Postgres
        init_connection_pool()
        conn = _pg_pool.getconn()
        try:
            yield conn
            conn.commit()
        except Exception as e:
            conn.rollback()
            from core.safe_logging import log_exception_safe
            log_exception_safe(logger, "Postgres DB error", e)
            raise
        finally:
            _pg_pool.putconn(conn)

def _dict_factory(cursor, row):
    """Custom dict factory for sqlite3 rows to match RealDictCursor behavior."""
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def _adapt_query(query: str) -> str:
    """Adapt SQL query for SQLite (replace %s with ?)."""
    if settings.DB_TYPE == "sqlite":
        return query.replace("%s", "?")
    return query

def _json_serialize(data: Any) -> Any:
    """Serialize data to JSON string if using SQLite, else return object for PG adapter."""
    if settings.DB_TYPE == "sqlite":
        return json.dumps(data) if data is not None else None
    return json.dumps(data) if data is not None else None # PG usually needs string unless using Json adapter

def init_database():
    """Initialize database schema and tables."""
    logger.info(f"Initializing database schema ({settings.DB_TYPE})...")
    with get_connection() as conn:
        cur = conn.cursor()
        try:
            # Type Abstractions
            if settings.DB_TYPE == "sqlite":
                PK_TYPE = "INTEGER PRIMARY KEY AUTOINCREMENT"
                JSON_TYPE = "TEXT"
                BOOL_TYPE = "BOOLEAN" # SQLite connects this to int, but declares fine
                TS_DEFAULT = "DEFAULT CURRENT_TIMESTAMP"
            else:
                PK_TYPE = "SERIAL PRIMARY KEY"
                JSON_TYPE = "JSONB"
                BOOL_TYPE = "BOOLEAN"
                TS_DEFAULT = "DEFAULT CURRENT_TIMESTAMP"

            # Create users table
            cur.execute(f"""
                CREATE TABLE IF NOT EXISTS users (
                    id {PK_TYPE},
                    username VARCHAR(50) UNIQUE NOT NULL,
                    password_hash VARCHAR(255) NOT NULL,
                    role VARCHAR(20) NOT NULL,
                    email VARCHAR(100),
                    created_at TIMESTAMP {TS_DEFAULT},
                    updated_at TIMESTAMP {TS_DEFAULT},
                    is_active {BOOL_TYPE} DEFAULT 1,
                    last_login TIMESTAMP
                )
            """)

            # Create sessions table
            cur.execute(f"""
                CREATE TABLE IF NOT EXISTS sessions (
                    id {PK_TYPE},
                    user_id INTEGER NOT NULL REFERENCES users(id),
                    session_token VARCHAR(255) UNIQUE NOT NULL,
                    created_at TIMESTAMP {TS_DEFAULT},
                    expires_at TIMESTAMP NOT NULL,
                    ip_address VARCHAR(45),
                    user_agent TEXT,
                    is_active {BOOL_TYPE} DEFAULT 1
                )
            """)

            # Create chat_history table
            cur.execute(f"""
                CREATE TABLE IF NOT EXISTS chat_history (
                    id {PK_TYPE},
                    user_id INTEGER NOT NULL REFERENCES users(id),
                    session_id INTEGER REFERENCES sessions(id),
                    role VARCHAR(20) NOT NULL,
                    content TEXT NOT NULL,
                    created_at TIMESTAMP {TS_DEFAULT},
                    metadata {JSON_TYPE}
                )
            """)

            # Create audit_logs table
            cur.execute(f"""
                CREATE TABLE IF NOT EXISTS audit_logs (
                    id {PK_TYPE},
                    user_id INTEGER REFERENCES users(id),
                    action VARCHAR(100) NOT NULL,
                    resource_type VARCHAR(50),
                    resource_id VARCHAR(100),
                    changes {JSON_TYPE},
                    created_at TIMESTAMP {TS_DEFAULT},
                    ip_address VARCHAR(45)
                )
            """)

            # Create analytics_events table
            cur.execute(f"""
                CREATE TABLE IF NOT EXISTS analytics_events (
                    id {PK_TYPE},
                    user_id INTEGER NOT NULL REFERENCES users(id),
                    event_type VARCHAR(50) NOT NULL,
                    event_name VARCHAR(100) NOT NULL,
                    data {JSON_TYPE},
                    created_at TIMESTAMP {TS_DEFAULT}
                )
            """)

            # Create Indexes
            if settings.DB_TYPE == "sqlite":
                 cur.execute("CREATE INDEX IF NOT EXISTS idx_chat_user_id ON chat_history(user_id)")
                 cur.execute("CREATE INDEX IF NOT EXISTS idx_analytics_user_id ON analytics_events(user_id)")
            else:
                 cur.execute("CREATE INDEX IF NOT EXISTS idx_chat_user_id ON chat_history(user_id)")
                 cur.execute("CREATE INDEX IF NOT EXISTS idx_analytics_user_id ON analytics_events(user_id)")

            conn.commit()
            logger.info("Database schema initialized successfully")
        except Exception as e:
            from core.safe_logging import log_exception_safe
            log_exception_safe(logger, "Failed to initialize schema", e)
            raise

def add_user(username: str, password_hash: str, role: str, email: Optional[str] = None) -> int:
    """Add a new user to the database."""
    with get_connection() as conn:
        cur = conn.cursor()
        try:
            query = _adapt_query("""
                INSERT INTO users (username, password_hash, role, email)
                VALUES (%s, %s, %s, %s)
            """)
            
            if settings.DB_TYPE == "postgres":
                 query += " RETURNING id"
                 cur.execute(query, (username, password_hash, role, email))
                 user_id = cur.fetchone()[0]
            else:
                 cur.execute(query, (username, password_hash, role, email))
                 user_id = cur.lastrowid
                 
            from core.safe_logging import mask_identifier
            logger.info(f"User created: {mask_identifier(username, 'user')} (ID: {mask_identifier(str(user_id), 'id')})")
            return user_id
        except Exception as e: # Catch IntegrityError equivalent
            from core.safe_logging import log_exception_safe
            log_exception_safe(logger, "User creation failed", e, level="warning")
            raise # Re-raise for controller handling if needed

def get_user(username: str) -> Optional[Dict[str, Any]]:
    """Get user by username."""
    with get_connection() as conn:
        if settings.DB_TYPE == "postgres":
            cur = conn.cursor(cursor_factory=RealDictCursor)
        else:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            
        cur.execute(_adapt_query(
            "SELECT id, username, password_hash, role, email, is_active "
            "FROM users WHERE username = %s"
        ), (username,))
        
        row = cur.fetchone()
        if row:
             return dict(row)
        return None

def update_last_login(user_id: int) -> None:
    """Update user's last login timestamp."""
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(_adapt_query(
            "UPDATE users SET last_login = CURRENT_TIMESTAMP WHERE id = %s"
        ), (user_id,))

def save_chat_message(
    user_id: int,
    role: str,
    content: str,
    session_id: Optional[int] = None,
    metadata: Optional[Dict] = None,
) -> int:
    """Save a chat message to the database."""
    with get_connection() as conn:
        cur = conn.cursor()
        metadata_json = _json_serialize(metadata)
        
        query = _adapt_query("""
            INSERT INTO chat_history
            (user_id, session_id, role, content, metadata)
            VALUES (%s, %s, %s, %s, %s)
        """)
        
        if settings.DB_TYPE == "postgres":
            query += " RETURNING id"
            cur.execute(query, (user_id, session_id, role, content, metadata_json))
            message_id = cur.fetchone()[0]
        else:
            cur.execute(query, (user_id, session_id, role, content, metadata_json))
            message_id = cur.lastrowid
            
        return message_id

def get_chat_history(
    user_id: int, limit: int = 100, offset: int = 0
) -> List[Dict[str, Any]]:
    """Get chat history for a user."""
    with get_connection() as conn:
        if settings.DB_TYPE == "postgres":
            cur = conn.cursor(cursor_factory=RealDictCursor)
        else:
            conn.row_factory = _dict_factory # Use dict wrapper for easier JSON handling
            cur = conn.cursor()
            
        cur.execute(_adapt_query("""
            SELECT id, role, content, created_at, metadata
            FROM chat_history
            WHERE user_id = %s
            ORDER BY created_at DESC
            LIMIT %s OFFSET %s
        """), (user_id, limit, offset))
        
        rows = cur.fetchall()
        
        # SQLite JSON handling (deserialize text back to dict)
        if settings.DB_TYPE == "sqlite":
             result = []
             for row in rows:
                 r = dict(row)
                 if r.get("metadata") and isinstance(r["metadata"], str):
                     try:
                         r["metadata"] = json.loads(r["metadata"])
                     except: 
                         pass
                 result.append(r)
             return result
             
        # Postgres already returns Dict if RealDictCursor handles JSONB? 
        # Actually psycopg2 returns dict for JSONB automatically.
        return [dict(r) for r in rows]

def clear_chat_history(user_id: int) -> int:
    """Clear all chat history for a user."""
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(_adapt_query(
            "DELETE FROM chat_history WHERE user_id = %s"
        ), (user_id,))
        return cur.rowcount

def log_audit_event(
    user_id: Optional[int],
    action: str,
    resource_type: Optional[str] = None,
    resource_id: Optional[str] = None,
    changes: Optional[Dict] = None,
    ip_address: Optional[str] = None,
) -> int:
    """Log an audit event."""
    with get_connection() as conn:
        cur = conn.cursor()
        changes_json = _json_serialize(changes)
        
        query = _adapt_query("""
            INSERT INTO audit_logs
            (user_id, action, resource_type, resource_id, changes, ip_address)
            VALUES (%s, %s, %s, %s, %s, %s)
        """)
        
        if settings.DB_TYPE == "postgres":
            query += " RETURNING id"
            cur.execute(query, (user_id, action, resource_type, resource_id, changes_json, ip_address))
            return cur.fetchone()[0]
        else:
            cur.execute(query, (user_id, action, resource_type, resource_id, changes_json, ip_address))
            return cur.lastrowid

def log_analytics_event(
    user_id: int, event_type: str, event_name: str, data: Optional[Dict] = None
) -> int:
    """Log an analytics event."""
    with get_connection() as conn:
        cur = conn.cursor()
        data_json = _json_serialize(data)
        
        query = _adapt_query("""
            INSERT INTO analytics_events
            (user_id, event_type, event_name, data)
            VALUES (%s, %s, %s, %s)
        """)
        
        if settings.DB_TYPE == "postgres":
             query += " RETURNING id"
             cur.execute(query, (user_id, event_type, event_name, data_json))
             return cur.fetchone()[0]
        else:
             cur.execute(query, (user_id, event_type, event_name, data_json))
             return cur.lastrowid


def get_analytics_summary(
    start_date: Optional[str] = None, end_date: Optional[str] = None
) -> Dict[str, Any]:
    """Get analytics summary for a date range."""
    with get_connection() as conn:
        if settings.DB_TYPE == "postgres":
             cur = conn.cursor(cursor_factory=RealDictCursor)
        else:
             conn.row_factory = sqlite3.Row
             cur = conn.cursor()
             
        query = _adapt_query("""
            SELECT
                COUNT(DISTINCT user_id) as unique_users,
                COUNT(*) as total_events,
                event_type,
                DATE(created_at) as event_date
            FROM analytics_events
            WHERE 1=1
        """)
        params = []

        if start_date:
            query += " AND created_at >= %s"
            params.append(start_date)

        if end_date:
            query += " AND created_at <= %s"
            params.append(end_date)

        query += " GROUP BY event_type, DATE(created_at) ORDER BY event_date DESC"

        cur.execute(query, params)
        rows = cur.fetchall()
        return [dict(r) for r in rows]

def get_top_users(limit: int = 5) -> List[Dict[str, Any]]:
    """Get top active users by event count."""
    with get_connection() as conn:
        if settings.DB_TYPE == "postgres":
             cur = conn.cursor(cursor_factory=RealDictCursor)
        else:
             conn.row_factory = sqlite3.Row
             cur = conn.cursor()
             
        # Join with users table to get usernames
        query = _adapt_query("""
            SELECT u.username, COUNT(a.id) as event_count
            FROM analytics_events a
            JOIN users u ON a.user_id = u.id
            GROUP BY u.username
            ORDER BY event_count DESC
            LIMIT %s
        """)
        
        cur.execute(query, (limit,))
        rows = cur.fetchall()
        return [dict(r) for r in rows]

def get_audit_logs(
    user_id: Optional[int] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    limit: int = 100,
) -> List[Dict[str, Any]]:
    """Get audit logs with optional filtering."""
    with get_connection() as conn:
        if settings.DB_TYPE == "postgres":
             cur = conn.cursor(cursor_factory=RealDictCursor)
        else:
             conn.row_factory = _dict_factory
             cur = conn.cursor()
             
        query = _adapt_query("SELECT * FROM audit_logs WHERE 1=1")
        params = []

        if user_id:
            query += " AND user_id = %s"
            params.append(user_id)

        if start_date:
            query += " AND created_at >= %s"
            params.append(start_date)

        if end_date:
            query += " AND created_at <= %s"
            params.append(end_date)

        query += " ORDER BY created_at DESC LIMIT %s"
        params.append(limit)

        cur.execute(query, params)
        rows = cur.fetchall()
        
        # JSON handling for SQLite
        if settings.DB_TYPE == "sqlite":
             result = []
             for row in rows:
                 r = dict(row)
                 if r.get("changes") and isinstance(r["changes"], str):
                     try:
                         r["changes"] = json.loads(r["changes"])
                     except: pass
                 result.append(r)
             return result
             
        return [dict(r) for r in rows]

def close_connection_pool():
    """Close all connections in the pool."""
    global _pg_pool
    if _pg_pool:
        _pg_pool.closeall()
        _pg_pool = None

