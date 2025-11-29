# 🚀 Phase 2 Enhancement Roadmap

## Overview

Phase 2 transforms the Nursing Validator from a single-instance application into an **enterprise-grade, scalable platform** with four major feature sets:

1. **Phase 2.1: PostgreSQL Database Integration** ✅ (In Progress)
2. **Phase 2.2: Advanced Analytics Dashboard**
3. **Phase 2.3: EHR/FHIR Integration**
4. **Phase 2.4: Mobile App (React Native)**

---

## Phase 2.1: PostgreSQL Database Integration

### Objective
Replace JSON file-based storage with a robust PostgreSQL database for production scalability.

### Features Implemented

#### Database Schema
```sql
users              - User accounts, roles, permissions
sessions           - Active sessions, expiry, tracking
chat_history       - Persistent conversation storage
audit_logs         - Security and compliance logging
analytics_events   - User behavior and feature usage
schema_migrations  - Migration versioning
```

#### Connection Management
- **Connection Pooling**: SimpleConnectionPool (min: 2, max: 20 connections)
- **Context Managers**: Automatic connection handling and cleanup
- **Error Recovery**: Rollback on failures, detailed logging

#### Features

1. **Multi-User Chat History**
   - Per-user conversation persistence
   - Full-text search ready (Postgres native)
   - Export capabilities

2. **Audit Logging**
   - All user actions logged with timestamp and IP
   - Change tracking with JSONB storage
   - Compliance-ready (HIPAA, GDPR)

3. **Analytics Events**
   - Track feature usage
   - Understand user behavior
   - Generate compliance reports

4. **Automated Backups**
   - Daily backup automation (pg_dump)
   - Retention policies (keep 30 days)
   - One-click restore functionality

### Setup Instructions

#### 1. Prerequisites

```bash
# Install PostgreSQL (if not already installed)
# macOS
brew install postgresql

# Ubuntu/Debian
sudo apt-get install postgresql postgresql-contrib

# Windows (via WSL or native installer)
choco install postgresql
```

#### 2. Create Database

```bash
# Connect to PostgreSQL as admin
sudo -u postgres psql

# Create database and user
CREATE DATABASE nursing_validator;
CREATE USER nursing_admin WITH PASSWORD 'change_me_in_production';
ALTER ROLE nursing_admin SET client_encoding TO 'utf8';
ALTER ROLE nursing_admin SET default_transaction_isolation TO 'read committed';
ALTER ROLE nursing_admin SET default_transaction_deferrable TO ON;
ALTER ROLE nursing_admin SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE nursing_validator TO nursing_admin;
\q
```

#### 3. Configure Environment

```bash
# Copy and update configuration
cp .env.production.example .env.production

# Edit .env.production with your database credentials
DB_HOST=localhost
DB_PORT=5432
DB_NAME=nursing_validator
DB_USER=nursing_admin
DB_PASSWORD=your_secure_password
DB_POOL_MIN=2
DB_POOL_MAX=20
BACKUP_DIR=/path/to/backups
USE_DATABASE=true
```

#### 4. Install Python Dependencies

```bash
pip install -r requirements.txt
# New packages added:
# - psycopg2-binary==2.9.9  (PostgreSQL adapter)
# - bcrypt==5.0.0           (Password hashing)
# - alembic==1.14.0         (Migration framework)
```

#### 5. Initialize Database

```bash
# Run migrations to create schema
python -c "from db_migrations import run_migrations; run_migrations()"

# Or in Python
from database import init_database
from db_migrations import run_migrations

init_database()
run_migrations()
```

#### 6. Run Application with Database

```bash
# Start with database backend
USE_DATABASE=true streamlit run app_phase2.py

# Or using the .env file
streamlit run app_phase2.py
```

### API Reference

#### Database Module (`database.py`)

```python
# Connection management
from database import init_connection_pool, get_connection

# Initialize once at startup
init_connection_pool()

# Use in context manager
with get_connection() as conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    results = cur.fetchall()
```

#### User Management

```python
from database import add_user, get_user, update_last_login

# Add new user
user_id = add_user(
    username="newuser",
    password_hash=hash_password("password"),
    role="nurse",
    email="nurse@hospital.com"
)

# Get user
user = get_user("username")

# Update last login
update_last_login(user_id)
```

#### Chat History

```python
from database import save_chat_message, get_chat_history, clear_chat_history

# Save message
message_id = save_chat_message(
    user_id=1,
    role="user",
    content="What is nursing care?",
    metadata={"source": "chat", "length": 25}
)

# Get history
history = get_chat_history(user_id=1, limit=100, offset=0)

# Clear history
deleted = clear_chat_history(user_id=1)
```

#### Audit Logging

```python
from database import log_audit_event, get_audit_logs

# Log event
event_id = log_audit_event(
    user_id=1,
    action="user_login",
    resource_type="user",
    resource_id="1",
    changes={"login_time": "2025-11-29T10:00:00"},
    ip_address="192.168.1.1"
)

# Get audit logs
logs = get_audit_logs(
    user_id=1,
    start_date="2025-11-01",
    end_date="2025-11-30",
    limit=100
)
```

#### Analytics

```python
from database import log_analytics_event, get_analytics_summary

# Log event
log_analytics_event(
    user_id=1,
    event_type="feature_usage",
    event_name="care_plan_view",
    data={"duration_seconds": 45}
)

# Get summary
summary = get_analytics_summary(
    start_date="2025-11-01",
    end_date="2025-11-30"
)
```

#### Backups

```python
from db_migrations import (
    create_backup,
    restore_backup,
    list_backups,
    cleanup_old_backups
)

# Create backup
backup_path = create_backup(backup_name="manual_backup.sql")

# List backups
backups = list_backups()

# Restore
restore_backup(backups[0])

# Clean up old ones (keep 10 most recent)
deleted = cleanup_old_backups(keep_count=10)
```

#### Migrations

```python
from db_migrations import run_migrations, rollback_migration

# Run all pending migrations
run_migrations()

# Rollback last 2 migrations
rollback_migration(steps=2)
```

### Database Architecture

```
┌─────────────────────────────────┐
│     Streamlit Application       │
│  (app_phase2.py)               │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│   Database Module Layer         │
│  (database.py)                  │
│                                 │
│  - Connection pooling           │
│  - ORM-like functions           │
│  - Context managers             │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│  Connection Pool                │
│  (psycopg2 SimpleConnectionPool)│
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│     PostgreSQL Database         │
│  - users                        │
│  - sessions                     │
│  - chat_history                 │
│  - audit_logs                   │
│  - analytics_events             │
│  - schema_migrations            │
└─────────────────────────────────┘
```

### Performance Considerations

#### Connection Pooling
- **Min Pool Size**: 2 (for low-traffic)
- **Max Pool Size**: 20 (for high-traffic)
- **Timeout**: 5 seconds per connection request
- **Recycle**: Connections reset after queries

#### Indexes
Automatic indexes created on:
- `sessions.user_id`
- `chat_history.user_id`
- `chat_history.created_at` (for time-range queries)
- `audit_logs.user_id`
- `analytics_events.user_id`

#### Query Optimization
- Pagination built-in (limit/offset)
- Prepared statements (psycopg2 parameterization)
- JSONB for flexible metadata

### Security Features

#### Authentication
- Password hashing with SHA-256 (upgrade to bcrypt for Phase 2.2)
- Session tokens with expiry
- IP address logging
- Failed login tracking

#### Authorization
- Role-based access control (RBAC)
- Per-user data isolation
- Admin-only operations flagged

#### Audit Trail
- All user actions logged
- Change tracking with JSONB
- Compliance reporting ready

#### Data Protection
- Automatic backups
- Disaster recovery procedures
- GDPR-compliant data retention

### Troubleshooting

#### Connection Errors
```python
# If you get "could not connect to server"
# Check PostgreSQL is running:
sudo service postgresql status

# Start if needed:
sudo service postgresql start

# Verify credentials in .env.production
```

#### Permission Errors
```sql
-- Reset user permissions
GRANT ALL PRIVILEGES ON DATABASE nursing_validator TO nursing_admin;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO nursing_admin;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO nursing_admin;
```

#### Backup Issues
```bash
# If pg_dump not found, install PostgreSQL client:
# macOS
brew install libpq

# Ubuntu
sudo apt-get install postgresql-client

# Add to PATH if needed
export PATH="/usr/lib/postgresql/XX/bin:$PATH"
```

### Migration Path from JSON

```python
# Script to migrate existing JSON chat history to PostgreSQL

import json
from database import add_user, save_chat_message, hash_password

# Load from JSON
with open('.chat_history.json', 'r') as f:
    json_data = json.load(f)

# Migrate each user's data
for username, messages in json_data.items():
    # Add user to database
    user_id = add_user(
        username=username,
        password_hash=hash_password("temp_password"),
        role="nurse"
    )
    
    # Migrate messages
    for msg in messages:
        save_chat_message(
            user_id=user_id,
            role=msg["role"],
            content=msg["content"]
        )

print(f"Migrated {len(json_data)} users to PostgreSQL")
```

### Next Steps

- Complete Phase 2.1 testing
- Deploy to staging with database
- Validate all migrations work
- Proceed to Phase 2.2: Analytics

### Files Added/Modified

**New Files:**
- `database.py` (365 lines) - Core database module
- `db_migrations.py` (250 lines) - Migration framework
- `app_phase2.py` (500 lines) - Updated app with DB support

**Modified Files:**
- `requirements.txt` - Added psycopg2-binary, bcrypt, alembic
- `.env.production.example` - Added database configuration

**Documentation:**
- `PHASE2_DATABASE.md` (this file)

---

## Next Phase: Phase 2.2 - Advanced Analytics Dashboard

After database integration is complete and tested, Phase 2.2 will add:
- Usage dashboards (who, what, when)
- Compliance reports
- Knowledge gap analysis
- Clinical outcome tracking

**Estimated Timeline:** 1-2 weeks

---

*Phase 2.1 Implementation - November 29, 2025*
