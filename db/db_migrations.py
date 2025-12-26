"""
Database migration and backup utilities for nursing validator.

Handles schema migrations, automated backups, and restoration.
"""

import os
import logging
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Optional, List

from core.settings import settings

logger = logging.getLogger(__name__)

# Backup configuration
BACKUP_DIR = os.getenv("BACKUP_DIR", "./backups")


def ensure_backup_dir():
    """Create backup directory if it doesn't exist."""
    Path(BACKUP_DIR).mkdir(parents=True, exist_ok=True)
    logger.info(f"Backup directory ready: {BACKUP_DIR}")


def create_backup(backup_name: Optional[str] = None) -> str:
    """Create a PostgreSQL database backup."""
    ensure_backup_dir()

    if backup_name is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"nursing_validator_{timestamp}.sql"

    backup_path = os.path.join(BACKUP_DIR, backup_name)

    try:
        env = os.environ.copy()
        env["PGPASSWORD"] = settings.DB_PASSWORD

        cmd = [
            "pg_dump",
            "-h",
            settings.DB_HOST,
            "-p",
            settings.DB_PORT,
            "-U",
            settings.DB_USER,
            "-d",
            settings.DB_NAME,
            "--file",
            backup_path,
            "--verbose",
        ]

        logger.info(f"Starting backup: {backup_path}")
        result = subprocess.run(cmd, env=env, capture_output=True, text=True)

        if result.returncode != 0:
            logger.error(f"Backup failed: {result.stderr}")
            raise Exception(f"pg_dump failed: {result.stderr}")

        file_size = os.path.getsize(backup_path) / (1024 * 1024)  # MB
        logger.info(f"Backup completed: {backup_path} ({file_size:.2f} MB)")
        return backup_path

    except FileNotFoundError:
        logger.error(
            "pg_dump not found. Please install PostgreSQL client tools."
        )
        raise
    except Exception as e:
        from core.safe_logging import log_exception_safe
        log_exception_safe(logger, "Backup error", e)
        raise


def restore_backup(backup_path: str) -> bool:
    """Restore database from a backup file."""
    if not os.path.exists(backup_path):
        logger.error(f"Backup file not found: {backup_path}")
        return False

    try:
        env = os.environ.copy()
        env["PGPASSWORD"] = settings.DB_PASSWORD

        cmd = [
            "psql",
            "-h",
            settings.DB_HOST,
            "-p",
            settings.DB_PORT,
            "-U",
            settings.DB_USER,
            "-d",
            settings.DB_NAME,
            "-f",
            backup_path,
        ]

        logger.info(f"Starting restore from: {backup_path}")
        result = subprocess.run(cmd, env=env, capture_output=True, text=True)

        if result.returncode != 0:
            logger.error(f"Restore failed: {result.stderr}")
            return False

        logger.info(f"Restore completed successfully")
        return True

    except FileNotFoundError:
        logger.error("psql not found. Please install PostgreSQL client tools.")
        return False
    except Exception as e:
        from core.safe_logging import log_exception_safe
        log_exception_safe(logger, "Restore error", e)
        return False


def list_backups() -> List[str]:
    """List all available backups."""
    ensure_backup_dir()
    backups = sorted(Path(BACKUP_DIR).glob("nursing_validator_*.sql"))
    return [str(b) for b in backups]


def cleanup_old_backups(keep_count: int = 10) -> int:
    """Delete old backups, keeping only the most recent."""
    ensure_backup_dir()
    backups = sorted(Path(BACKUP_DIR).glob("nursing_validator_*.sql"))

    if len(backups) <= keep_count:
        logger.info(f"Keeping {len(backups)} backups (under limit of {keep_count})")
        return 0

    to_delete = backups[:-keep_count]
    deleted_count = 0

    for backup in to_delete:
        try:
            backup.unlink()
            deleted_count += 1
            logger.info(f"Deleted old backup: {backup.name}")
        except Exception as e:
            from core.safe_logging import log_exception_safe
            log_exception_safe(logger, "Failed to delete backup file", e, level="warning")

    logger.info(f"Cleaned up {deleted_count} old backups")
    return deleted_count


class Migration:
    """Base class for database migrations."""

    version: int = 0
    description: str = ""

    def up(self):
        """Apply migration."""
        raise NotImplementedError

    def down(self):
        """Rollback migration."""
        raise NotImplementedError


class Migration001CreateInitialSchema(Migration):
    """Initial schema creation."""

    version = 1
    description = "Create initial schema with users, sessions, chat_history, audit_logs"

    def up(self):
        """Create initial tables."""
        from db.database import init_database

        init_database()
        logger.info("Migration 001: Schema created")

    def down(self):
        """Drop tables."""
        from db.database import get_connection

        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute("DROP TABLE IF EXISTS analytics_events CASCADE")
            cur.execute("DROP TABLE IF EXISTS audit_logs CASCADE")
            cur.execute("DROP TABLE IF EXISTS chat_history CASCADE")
            cur.execute("DROP TABLE IF EXISTS sessions CASCADE")
            cur.execute("DROP TABLE IF EXISTS users CASCADE")
            logger.info("Migration 001: Schema dropped")


class Migration002AddAnalyticsTables(Migration):
    """Add analytics tables."""

    version = 2
    description = "Add analytics_events and related tables"

    def up(self):
        """Create analytics tables."""
        from db.database import init_database

        init_database()
        logger.info("Migration 002: Analytics tables added")

    def down(self):
        """Drop analytics tables."""
        from db.database import get_connection

        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute("DROP TABLE IF EXISTS analytics_events CASCADE")
            logger.info("Migration 002: Analytics tables removed")


def get_migrations() -> List[Migration]:
    """Get all available migrations."""
    return [
        Migration001CreateInitialSchema(),
        Migration002AddAnalyticsTables(),
    ]


def run_migrations() -> bool:
    """Run all pending migrations."""
    from db.database import get_connection

    logger.info("Starting migration process...")

    try:
        with get_connection() as conn:
            cur = conn.cursor()

            # Create migrations table if it doesn't exist
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS schema_migrations (
                    id SERIAL PRIMARY KEY,
                    version INTEGER UNIQUE NOT NULL,
                    description VARCHAR(255),
                    applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """
            )

            # Get applied migrations
            cur.execute("SELECT version FROM schema_migrations ORDER BY version")
            applied = {row[0] for row in cur.fetchall()}

            # Run pending migrations
            for migration in get_migrations():
                if migration.version not in applied:
                    logger.info(
                        f"Running migration {migration.version}: "
                        f"{migration.description}"
                    )
                    migration.up()

                    cur.execute(
                        """
                        INSERT INTO schema_migrations (version, description)
                        VALUES (%s, %s)
                    """,
                        (migration.version, migration.description),
                    )

        logger.info("All migrations completed successfully")
        return True

    except Exception as e:
        from core.safe_logging import log_exception_safe
        log_exception_safe(logger, "Migration failed", e)
        return False


def rollback_migration(steps: int = 1) -> bool:
    """Rollback N migrations."""
    from db.database import get_connection

    logger.info(f"Rolling back {steps} migration(s)...")

    try:
        with get_connection() as conn:
            cur = conn.cursor()

            # Get applied migrations
            cur.execute(
                "SELECT version FROM schema_migrations "
                "ORDER BY version DESC LIMIT %s",
                (steps,),
            )
            to_rollback = [row[0] for row in cur.fetchall()]

            # Rollback in reverse order
            migrations_map = {m.version: m for m in get_migrations()}
            for version in to_rollback:
                if version in migrations_map:
                    logger.info(f"Rolling back migration {version}")
                    migrations_map[version].down()

                    cur.execute(
                        "DELETE FROM schema_migrations WHERE version = %s",
                        (version,),
                    )

        logger.info(f"Rolled back {len(to_rollback)} migration(s)")
        return True

    except Exception as e:
        from core.safe_logging import log_exception_safe
        log_exception_safe(logger, "Rollback failed", e)
        return False
