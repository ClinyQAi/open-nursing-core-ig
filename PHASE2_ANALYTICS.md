# Phase 2.2: Advanced Analytics Dashboard

## Overview

**Phase 2.2** transforms the application into an **analytics-driven platform** with comprehensive insights into system usage, clinical outcomes, compliance, and knowledge gaps.

**Prerequisite:** Phase 2.1 (PostgreSQL Database) must be completed

### Features

#### 1. **📊 Analytics Overview**
- Real-time key metrics
- Active users count
- Active sessions
- Total messages processed
- 24-hour event summary

#### 2. **📈 Usage Analytics**
- Daily active user trends
- Top users by message count
- Usage patterns over time
- Feature adoption metrics

#### 3. **📋 Compliance Reporting**
- Login/logout audit trails
- Failed login tracking
- Data access audit logs
- HIPAA/GDPR compliance ready
- 90-day historical reporting

#### 4. **🔍 Knowledge Gap Analysis**
- Question distribution by topic
- Unanswered query tracking
- Low-confidence answer detection
- Content recommendations

#### 5. **🏥 Clinical Outcomes**
- Care plan duration metrics
- Goal achievement rates
- Patient satisfaction scores
- Clinical outcome trends

#### 6. **👥 User Activity Report**
- Per-user engagement metrics
- Last login tracking
- Message and session counts
- Role-based usage analysis

#### 7. **⚙️ System Health**
- Database status
- API response times
- Vector database readiness
- System uptime tracking

---

## Setup Instructions

### Prerequisites

1. **Phase 2.1 Completed**
   - PostgreSQL database running
   - Chat history in database
   - Audit logs populated

2. **Python Packages**
   ```bash
   pip install pandas plotly streamlit
   ```
   (Already in requirements.txt)

### Configuration

```bash
# Update .env.production
export APP_ENV=production
export USE_DATABASE=true
export DB_HOST=localhost
export DB_PORT=5432
export DB_NAME=nursing_validator
export DB_USER=nursing_admin
export DB_PASSWORD=your_password
```

### Running Analytics

```bash
# Create analytics-only dashboard
streamlit run analytics_dashboard.py

# Or add analytics tab to main app
streamlit run app_phase2.py
# Then navigate to Analytics tab (admin only)
```

---

## Architecture

```
┌──────────────────────────────────────┐
│   Streamlit Analytics Frontend       │
│   (analytics_dashboard.py)           │
├──────────────────────────────────────┤
│  Overview│Usage│Compliance│Gaps...  │
├──────────────────────────────────────┤
│      AnalyticsDashboard Class        │
│   - display_overview()               │
│   - display_usage_dashboard()        │
│   - display_compliance_report()      │
│   - display_knowledge_gaps()         │
│   - display_clinical_outcomes()      │
│   - display_user_activity()          │
│   - display_system_health()          │
├──────────────────────────────────────┤
│        Data Processing Layer         │
│   (pandas + plotly visualization)    │
├──────────────────────────────────────┤
│      Database Query Layer            │
│   (database.py - via SQL)            │
├──────────────────────────────────────┤
│      PostgreSQL Database             │
│   ├─ chat_history                   │
│   ├─ audit_logs                     │
│   ├─ analytics_events               │
│   ├─ users                          │
│   └─ sessions                       │
└──────────────────────────────────────┘
```

---

## API Reference

### AnalyticsDashboard Class

```python
from analytics_dashboard import AnalyticsDashboard

# Initialize
dashboard = AnalyticsDashboard()

# Display sections
dashboard.display_overview()           # Key metrics
dashboard.display_usage_dashboard()    # Usage trends
dashboard.display_compliance_report()  # Audit logs
dashboard.display_knowledge_gaps()     # Content analysis
dashboard.display_clinical_outcomes()  # Patient metrics
dashboard.display_user_activity()      # Per-user stats
dashboard.display_system_health()      # System metrics
dashboard.display_export_options()     # Data export
```

### Integration with Main App

```python
# In app_phase2.py, add analytics tab

with tab_analytics:
    from analytics_dashboard import display_analytics_dashboard
    
    # Only for admin users
    if st.session_state.role == "admin":
        display_analytics_dashboard()
    else:
        st.warning("Analytics available for admins only")
```

---

## Reports

### 1. Overview Report

**Metrics:**
- Active Users: Count of users with is_active = TRUE
- Active Sessions: Count where expires_at > NOW
- Total Messages: COUNT(*) from chat_history
- Events (24h): Audit logs in last 24 hours

```sql
SELECT COUNT(*) FROM users WHERE is_active = TRUE;
SELECT COUNT(*) FROM sessions WHERE expires_at > CURRENT_TIMESTAMP;
SELECT COUNT(*) FROM chat_history;
SELECT COUNT(*) FROM audit_logs 
WHERE created_at > CURRENT_TIMESTAMP - INTERVAL '24 hours';
```

### 2. Usage Report

**Data:**
- Daily active users (line chart)
- Top 10 users by message count (bar chart)
- Time-range filtering (default: 30 days)

```sql
-- Daily active users
SELECT DATE(created_at), COUNT(DISTINCT user_id)
FROM chat_history
GROUP BY DATE(created_at);

-- Top users
SELECT u.username, COUNT(*)
FROM chat_history ch
JOIN users u ON ch.user_id = u.id
GROUP BY u.username
ORDER BY COUNT(*) DESC LIMIT 10;
```

### 3. Compliance Report

**Audit Events:**
- Login/logout tracking
- Failed login counts
- Data access by resource
- 90-day historical logs
- HIPAA compliance ready

```sql
-- Authentication events
SELECT action, COUNT(*), COUNT(DISTINCT user_id)
FROM audit_logs
WHERE action IN ('login', 'logout', 'failed_login')
GROUP BY action;

-- Data access
SELECT resource_type, COUNT(*), COUNT(DISTINCT user_id)
FROM audit_logs
WHERE resource_type IS NOT NULL
GROUP BY resource_type;
```

### 4. Knowledge Gap Analysis

**Analysis:**
- Question distribution by topic
- Topics: Care, Assessment, Interventions, Goals, Medications
- Pie chart of question types
- Identifies training needs

```sql
SELECT
    CASE
        WHEN content ILIKE '%care%' THEN 'Care Planning'
        WHEN content ILIKE '%assessment%' THEN 'Assessment'
        WHEN content ILIKE '%intervention%' THEN 'Interventions'
        WHEN content ILIKE '%goal%' THEN 'Goals'
        WHEN content ILIKE '%medication%' THEN 'Medications'
        ELSE 'Other'
    END as topic,
    COUNT(*)
FROM chat_history
WHERE role = 'user'
GROUP BY topic;
```

### 5. User Activity Report

**Metrics:**
- Username, role, last login
- Message count per user
- Session count
- Active in last 7 days count
- Average messages per user

```sql
SELECT
    u.username, u.role, u.last_login,
    COUNT(DISTINCT ch.id) as messages,
    COUNT(DISTINCT s.id) as sessions
FROM users u
LEFT JOIN chat_history ch ON u.id = ch.user_id
LEFT JOIN sessions s ON u.id = s.user_id
WHERE u.is_active = TRUE
GROUP BY u.id, u.username, u.role, u.last_login;
```

---

## Visualizations

### Line Chart: Daily Active Users
- **X-axis:** Date
- **Y-axis:** Number of unique users
- **Time Range:** Selectable (default: 30 days)
- **Type:** Line chart with markers

### Bar Chart: Top Users
- **X-axis:** Username
- **Y-axis:** Message count
- **Color:** Blue gradient (by message count)
- **Limit:** Top 10 users

### Pie Chart: Question Topics
- **Segments:** By topic (Care, Assessment, etc.)
- **Size:** Proportion of questions
- **Interactive:** Hover for details

### DataFrames: Audit Logs
- **Columns:** Timestamp, User, Action, Resource, IP
- **Sorting:** Reverse chronological
- **Limit:** 50 most recent
- **Filterable:** By date range

---

## Compliance Features

### HIPAA Compliance Ready
- ✅ Audit trails for all data access
- ✅ User authentication logging
- ✅ Encryption ready (TLS)
- ✅ Data retention policies configurable
- ✅ IP address logging for accountability

### GDPR Compliance Ready
- ✅ User activity tracking
- ✅ Data access audit logs
- ✅ Right to be forgotten support (can delete user)
- ✅ Data export capabilities
- ✅ Consent management ready

### Audit Trail
All user actions logged with:
- Timestamp (UTC)
- User ID
- Action type
- Resource type/ID
- IP address
- Changes (JSONB format)

---

## Data Export

### Export Formats (Ready for Phase 2.3)

#### CSV Export
```python
df.to_csv('analytics_report.csv', index=False)
```

#### PDF Export
```python
# Uses plotly for static image export
fig.write_image("report.pdf")
```

#### Excel Export
```python
df.to_excel('analytics_report.xlsx', sheet_name='Analytics')
```

### Sample Export Query

```python
import pandas as pd
from database import get_connection

# Export user activity
with get_connection() as conn:
    df = pd.read_sql_query("""
        SELECT u.username, u.role, COUNT(*) as messages
        FROM chat_history ch
        JOIN users u ON ch.user_id = u.id
        GROUP BY u.id, u.username, u.role
    """, conn)
    
    df.to_excel('user_activity.xlsx')
    df.to_csv('user_activity.csv')
```

---

## Troubleshooting

### "Database required for analytics"
```
Error: Database module not available
Solution: Install psycopg2-binary
$ pip install psycopg2-binary
```

### No data showing in charts
```
Possible causes:
1. No chat history yet (new database)
2. Time range filters with no data
3. Database connection issue

Debug:
SELECT COUNT(*) FROM chat_history;
SELECT COUNT(*) FROM users;
SELECT COUNT(*) FROM audit_logs;
```

### Slow dashboard loading
```
Solutions:
1. Add indexes (already done in Phase 2.1)
2. Limit time range (default 30 days)
3. Increase database pool size
4. Cache results for 5 minutes
```

### Connection timeouts
```
Fix timeout:
DB_HOST=localhost
DB_PORT=5432
# Verify PostgreSQL running:
sudo service postgresql status
sudo service postgresql start
```

---

## Performance Optimization

### Database Indexes
Already created in Phase 2.1:
```sql
CREATE INDEX idx_chat_history_created_at ON chat_history(created_at);
CREATE INDEX idx_analytics_user_id ON analytics_events(user_id);
CREATE INDEX idx_audit_logs_user_id ON audit_logs(user_id);
```

### Query Caching
```python
@st.cache_data(ttl=300)  # Cache for 5 minutes
def get_dashboard_data():
    # Expensive query here
    pass
```

### Pagination
```python
# Limit audit logs to 50 most recent
LIMIT 50 OFFSET (page - 1) * 50
```

---

## Next Steps

1. **Deploy Phase 2.2** to staging
2. **Test analytics queries** with sample data
3. **Validate compliance reports** meet requirements
4. **Proceed to Phase 2.3** - EHR/FHIR Integration

---

## Files Created/Modified

**New Files:**
- `analytics_dashboard.py` (400+ lines)

**Integration Points:**
- Update `app_phase2.py` to add analytics tab
- Add analytics logging to chat module

**Documentation:**
- `PHASE2_ANALYTICS.md` (this file)

---

*Phase 2.2 Implementation - November 29, 2025*
