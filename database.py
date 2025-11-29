"""
PostgreSQL database module for NHS Unified Nursing Validator.

Provides database connection pooling, schema management, and ORM operations
for chat history, users, sessions, and audit logs.
"""

import os
import json
import logging
from datetime import datetime
from typing import Optional, List, Dict, Any
from contextlib import contextmanager

import psycopg2
from psycopg2 import pool, sql
from psycopg2.extras import RealDictCursor, execute_values

logger = logging.getLogger(__name__)

# Database configuration from environment
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "nursing_validator")
DB_USER = os.getenv("DB_USER", "nursing_admin")
DB_PASSWORD = os.getenv("DB_PASSWORD", "nursing_password")
DB_POOL_MIN = int(os.getenv("DB_POOL_MIN", "2"))
DB_POOL_MAX = int(os.getenv("DB_POOL_MAX", "20"))

# Connection pool (initialized on first use)
_connection_pool = None


def init_connection_pool():
    """Initialize the PostgreSQL connection pool."""
    global _connection_pool
    if _connection_pool is None:
        try:
            _connection_pool = psycopg2.pool.SimpleConnectionPool(
                DB_POOL_MIN,
                DB_POOL_MAX,
                host=DB_HOST,
                port=DB_PORT,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD,
                connect_timeout=5,
            )
            logger.info("Database connection pool initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize connection pool: {e}")
            raise
    return _connection_pool


@contextmanager
def get_connection():
    """Context manager for database connections."""
    pool = init_connection_pool()
    conn = pool.getconn()
    try:
        yield conn
        conn.commit()
    except Exception as e:
        conn.rollback()
        logger.error(f"Database error: {e}", exc_info=True)
        raise
    finally:
        pool.putconn(conn)


def init_database():
    """Initialize database schema and tables."""
    logger.info("Initializing database schema...")
    with get_connection() as conn:
        cur = conn.cursor()
        try:
            # Create users table
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(50) UNIQUE NOT NULL,
                    password_hash VARCHAR(255) NOT NULL,
                    role VARCHAR(20) NOT NULL,
                    email VARCHAR(100),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    is_active BOOLEAN DEFAULT TRUE,
                    last_login TIMESTAMP
                )
            """)

            # Create sessions table
            cur.execute("""
                CREATE TABLE IF NOT EXISTS sessions (
                    id SERIAL PRIMARY KEY,
                    user_id INTEGER NOT NULL REFERENCES users(id),
                    session_token VARCHAR(255) UNIQUE NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    expires_at TIMESTAMP NOT NULL,
                    ip_address VARCHAR(45),
                    user_agent TEXT,
                    is_active BOOLEAN DEFAULT TRUE
                )
            """)

            # Create chat_history table
            cur.execute("""
                CREATE TABLE IF NOT EXISTS chat_history (
                    id SERIAL PRIMARY KEY,
                    user_id INTEGER NOT NULL REFERENCES users(id),
                    session_id INTEGER REFERENCES sessions(id),
                    role VARCHAR(20) NOT NULL,
                    content TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    metadata JSONB
                )
            """)

            # Create audit_logs table
            cur.execute("""
                CREATE TABLE IF NOT EXISTS audit_logs (
                    id SERIAL PRIMARY KEY,
                    user_id INTEGER REFERENCES users(id),
                    action VARCHAR(100) NOT NULL,
                    resource_type VARCHAR(50),
                    resource_id VARCHAR(100),
                    changes JSONB,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    ip_address VARCHAR(45)
                )
            """)

            # Create analytics_events table
            cur.execute("""
                CREATE TABLE IF NOT EXISTS analytics_events (
                    id SERIAL PRIMARY KEY,
                    user_id INTEGER NOT NULL REFERENCES users(id),
                    event_type VARCHAR(50) NOT NULL,
                    event_name VARCHAR(100) NOT NULL,
                    data JSONB,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

            # Create indexes for performance
            cur.execute(
                "CREATE INDEX IF NOT EXISTS idx_sessions_user_id "
                "ON sessions(user_id)"
            )
            cur.execute(
                "CREATE INDEX IF NOT EXISTS idx_chat_history_user_id "
                "ON chat_history(user_id)"
            )
            cur.execute(
                "CREATE INDEX IF NOT EXISTS idx_chat_history_created_at "
                "ON chat_history(created_at)"
            )
            cur.execute(
                "CREATE INDEX IF NOT EXISTS idx_audit_logs_user_id "
                "ON audit_logs(user_id)"
            )
            cur.execute(
                "CREATE INDEX IF NOT EXISTS idx_analytics_user_id "
                "ON analytics_events(user_id)"
            )

            conn.commit()
            logger.info("Database schema initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize schema: {e}", exc_info=True)
            raise


def add_user(
    username: str, password_hash: str, role: str, email: Optional[str] = None
) -> int:
    """Add a new user to the database."""
    with get_connection() as conn:
        cur = conn.cursor()
        try:
            cur.execute(
                """
                INSERT INTO users (username, password_hash, role, email)
                VALUES (%s, %s, %s, %s)
                RETURNING id
                """,
                (username, password_hash, role, email),
            )
            user_id = cur.fetchone()[0]
            logger.info(f"User created: {username} (ID: {user_id})")
            return user_id
        except psycopg2.IntegrityError:
            logger.warning(f"User already exists: {username}")
            raise


def get_user(username: str) -> Optional[Dict[str, Any]]:
    """Get user by username."""
    with get_connection() as conn:
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(
            "SELECT id, username, password_hash, role, email, is_active "
            "FROM users WHERE username = %s",
            (username,),
        )
        return cur.fetchone()


def update_last_login(user_id: int) -> None:
    """Update user's last login timestamp."""
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            "UPDATE users SET last_login = CURRENT_TIMESTAMP WHERE id = %s",
            (user_id,),
        )
        logger.debug(f"Updated last_login for user {user_id}")


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
        try:
            metadata_json = json.dumps(metadata) if metadata else None
            cur.execute(
                """
                INSERT INTO chat_history
                (user_id, session_id, role, content, metadata)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING id
                """,
                (user_id, session_id, role, content, metadata_json),
            )
            message_id = cur.fetchone()[0]
            return message_id
        except Exception as e:
            logger.error(f"Failed to save chat message: {e}", exc_info=True)
            raise


def get_chat_history(
    user_id: int, limit: int = 100, offset: int = 0
) -> List[Dict[str, Any]]:
    """Get chat history for a user."""
    with get_connection() as conn:
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(
            """
            SELECT id, role, content, created_at, metadata
            FROM chat_history
            WHERE user_id = %s
            ORDER BY created_at DESC
            LIMIT %s OFFSET %s
            """,
            (user_id, limit, offset),
        )
        return cur.fetchall()


def clear_chat_history(user_id: int) -> int:
    """Clear all chat history for a user."""
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM chat_history WHERE user_id = %s", (user_id,)
        )
        deleted_count = cur.rowcount
        logger.info(f"Cleared {deleted_count} messages for user {user_id}")
        return deleted_count


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
        changes_json = json.dumps(changes) if changes else None
        cur.execute(
            """
            INSERT INTO audit_logs
            (user_id, action, resource_type, resource_id, changes, ip_address)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING id
            """,
            (user_id, action, resource_type, resource_id, changes_json, ip_address),
        )
        event_id = cur.fetchone()[0]
        return event_id


def log_analytics_event(
    user_id: int,
    event_type: str,
    event_name: str,
    data: Optional[Dict] = None,
) -> int:
    """Log an analytics event."""
    with get_connection() as conn:
        cur = conn.cursor()
        data_json = json.dumps(data) if data else None
        cur.execute(
            """
            INSERT INTO analytics_events
            (user_id, event_type, event_name, data)
            VALUES (%s, %s, %s, %s)
            RETURNING id
            """,
            (user_id, event_type, event_name, data_json),
        )
        event_id = cur.fetchone()[0]
        return event_id


def get_analytics_summary(
    start_date: Optional[str] = None, end_date: Optional[str] = None
) -> Dict[str, Any]:
    """Get analytics summary for a date range."""
    with get_connection() as conn:
        cur = conn.cursor(cursor_factory=RealDictCursor)
        query = """
            SELECT
                COUNT(DISTINCT user_id) as unique_users,
                COUNT(*) as total_events,
                event_type,
                DATE(created_at) as event_date
            FROM analytics_events
        """
        params = []

        if start_date:
            query += " WHERE created_at >= %s"
            params.append(start_date)

        if end_date:
            query += f" {'AND' if start_date else 'WHERE'} created_at <= %s"
            params.append(end_date)

        query += " GROUP BY event_type, DATE(created_at) ORDER BY event_date DESC"

        cur.execute(query, params)
        return cur.fetchall()


def get_audit_logs(
    user_id: Optional[int] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    limit: int = 100,
) -> List[Dict[str, Any]]:
    """Get audit logs with optional filtering."""
    with get_connection() as conn:
        cur = conn.cursor(cursor_factory=RealDictCursor)
        query = "SELECT * FROM audit_logs WHERE 1=1"
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
        return cur.fetchall()


def close_connection_pool():
    """Close all connections in the pool."""
    global _connection_pool
    if _connection_pool:
        _connection_pool.closeall()
        _connection_pool = None
        logger.info("Connection pool closed")
