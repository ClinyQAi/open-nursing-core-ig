
import pandas as pd
import altair as alt
import streamlit as st
import json
from datetime import datetime, timedelta
from db.database import get_analytics_summary, get_top_users, get_audit_logs

def render_dashboard():
    """Render the advanced analytics dashboard."""
    st.title("📊 Advanced Analytics Dashboard")
    
    # Date Range Filter
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime.now() - timedelta(days=30))
    with col2:
        end_date = st.date_input("End Date", datetime.now())
        
    s_str = start_date.strftime("%Y-%m-%d")
    e_str = end_date.strftime("%Y-%m-%d")

    # Fetch Data
    summary_data = get_analytics_summary(start_date=s_str, end_date=e_str)
    
    # KPI Cards
    total_events = sum(d['total_events'] for d in summary_data)
    unique_users = sum(d['unique_users'] for d in summary_data) # Approximation
    
    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric("Total Events", total_events)
    # kpi2.metric("Active Users", unique_users) 
    
    # Tabs
    tab1, tab2, tab3 = st.tabs(["📉 Overview", "👥 User Engagement", "🛡️ Compliance & Audit"])
    
    with tab1:
        st.subheader("Event Trends")
        if summary_data:
            df = pd.DataFrame(summary_data)
            # Ensure proper types
            df['total_events'] = df['total_events'].astype(int)
            
            # Line Chart: Events over time by Type
            chart = alt.Chart(df).mark_line(point=True).encode(
                x='event_date:T',
                y='total_events:Q',
                color='event_type:N',
                tooltip=['event_date', 'event_type', 'total_events']
            ).interactive()
            
            st.altair_chart(chart, use_container_width=True)
            
            # Bar Chart: Distribution
            st.subheader("Event Distribution")
            bar = alt.Chart(df).mark_bar().encode(
                x='event_type:N',
                y='sum(total_events):Q',
                color='event_type:N',
                tooltip=['event_type', 'sum(total_events)']
            )
            st.altair_chart(bar, use_container_width=True)
        else:
            st.info("No data available for this range.")

    with tab2:
        st.subheader("Top Active Users")
        top_users = get_top_users(limit=10)
        if top_users:
            top_df = pd.DataFrame(top_users)
            st.table(top_df)
            
            user_chart = alt.Chart(top_df).mark_bar().encode(
                x='event_count:Q',
                y=alt.Y('username:N', sort='-x'),
                tooltip=['username', 'event_count']
            )
            st.altair_chart(user_chart, use_container_width=True)
        else:
            st.info("No user activity recorded.")

    with tab3:
        st.subheader("Security Audit Logs")
        
        # Filters
        uid_filter = st.text_input("Filter by User ID (Optional)")
        uid = int(uid_filter) if uid_filter.isdigit() else None
        
        audit_logs = get_audit_logs(user_id=uid, start_date=s_str, end_date=e_str, limit=50)
        
        if audit_logs:
            audit_df = pd.DataFrame(audit_logs)
            
            # Expand JSON changes for readability
            if 'changes' in audit_df.columns:
                audit_df['changes'] = audit_df['changes'].apply(lambda x: json.dumps(x) if isinstance(x, (dict, list)) else str(x))
                
            st.dataframe(
                audit_df[['created_at', 'action', 'resource_type', 'user_id', 'ip_address', 'changes']],
                use_container_width=True
            )
            
            csv = audit_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                "Download Audit Logs (CSV)",
                csv,
                "audit_logs.csv",
                "text/csv",
                key='download-csv'
            )
        else:
            st.info("No audit logs found.")
