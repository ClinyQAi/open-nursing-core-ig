"""
Visualization module for nursing care plans and assessments.
Provides charts and visualizations for clinical data.
"""
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


def create_care_plan_timeline(care_plan_data):
    """
    Create a timeline visualization for care plan interventions.

    Args:
        care_plan_data: List of interventions with dates

    Returns:
        Plotly figure
    """
    if not care_plan_data:
        return None

    df = pd.DataFrame(care_plan_data)
    fig = px.timeline(
        df,
        x_start="start_date",
        x_end="end_date",
        y="intervention",
        color="status",
        title="Care Plan Timeline",
        labels={"intervention": "Intervention", "status": "Status"}
    )
    fig.update_xaxes(type="date")
    return fig


def create_assessment_radar(assessment_scores):
    """
    Create a radar chart for multiple assessment domains.

    Args:
        assessment_scores: Dict with domain names and scores (0-100)

    Returns:
        Plotly figure
    """
    if not assessment_scores:
        return None

    categories = list(assessment_scores.keys())
    values = list(assessment_scores.values())

    fig = go.Figure(data=go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Assessment Score'
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(
            visible=True,
            range=[0, 100]
        )),
        title="Clinical Assessment Profile",
        showlegend=True
    )
    return fig


def create_health_indicators_gauge(
    indicator_name,
    current_value,
    target_value
):
    """
    Create a gauge chart for health indicators.

    Args:
        indicator_name: Name of the health indicator
        current_value: Current value
        target_value: Target value

    Returns:
        Plotly figure
    """
    fig = go.Figure(data=go.Indicator(
        mode="gauge+number+delta",
        value=current_value,
        delta={'reference': target_value},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 33], 'color': "lightgray"},
                {'range': [33, 66], 'color': "gray"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': target_value
            }
        },
        title={'text': indicator_name}
    ))
    return fig


def create_problem_severity_chart(problems):
    """
    Create a bar chart showing problem severity.

    Args:
        problems: List of dict with 'name' and 'severity' (0-10)

    Returns:
        Plotly figure
    """
    if not problems:
        return None

    df = pd.DataFrame(problems)
    fig = px.bar(
        df,
        x="severity",
        y="name",
        orientation="h",
        color="severity",
        color_continuous_scale="Reds",
        title="Nursing Problem Severity Assessment",
        labels={"severity": "Severity Score", "name": "Problem"}
    )
    return fig


def create_goal_progress_chart(goals):
    """
    Create a progress bar chart for care goals.

    Args:
        goals: List of dict with 'goal_name' and 'progress' (0-100)

    Returns:
        Plotly figure
    """
    if not goals:
        return None

    df = pd.DataFrame(goals)
    fig = px.bar(
        df,
        x="progress",
        y="goal_name",
        orientation="h",
        color="progress",
        color_continuous_scale="Greens",
        title="Care Goal Progress",
        labels={"progress": "Progress (%)", "goal_name": "Goal"}
    )
    return fig


def create_intervention_effectiveness_chart(interventions):
    """
    Create a chart showing intervention effectiveness.

    Args:
        interventions: List of dict with 'intervention' and 'effectiveness'

    Returns:
        Plotly figure
    """
    if not interventions:
        return None

    df = pd.DataFrame(interventions)
    fig = px.scatter(
        df,
        x="duration_days",
        y="effectiveness",
        size="patient_benefit",
        color="category",
        hover_name="intervention",
        title="Intervention Effectiveness Analysis",
        labels={
            "duration_days": "Duration (Days)",
            "effectiveness": "Effectiveness Score",
            "category": "Category"
        }
    )
    return fig


def create_risk_assessment_heatmap(risks):
    """
    Create a heatmap for risk assessment.

    Args:
        risks: 2D list with risk scores

    Returns:
        Plotly figure
    """
    fig = px.imshow(
        risks,
        labels=dict(
            x="Risk Factor",
            y="Patient ID",
            color="Risk Level"
        ),
        color_continuous_scale="YlOrRd",
        title="Risk Assessment Heatmap"
    )
    return fig


def display_care_plan_dashboard():
    """Display a comprehensive care plan dashboard."""
    st.subheader("📋 Care Plan Dashboard")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Active Care Goals",
            5,
            delta="+2 this week",
            delta_color="normal"
        )

    with col2:
        st.metric(
            "Goal Achievement Rate",
            "78%",
            delta="+5%",
            delta_color="off"
        )

    st.divider()

    # Sample care plan data
    sample_goals = [
        {"goal_name": "Pain Management", "progress": 85},
        {"goal_name": "Mobility Improvement", "progress": 60},
        {"goal_name": "Nutritional Intake", "progress": 92},
        {"goal_name": "Wound Healing", "progress": 45},
        {"goal_name": "Patient Education", "progress": 78}
    ]

    fig_goals = create_goal_progress_chart(sample_goals)
    if fig_goals:
        st.plotly_chart(fig_goals, use_container_width=True)

    st.divider()

    # Assessment scores
    sample_assessment = {
        "Mobility": 65,
        "Nutrition": 78,
        "Continence": 45,
        "Mental Health": 82,
        "Pain": 35,
        "Communication": 90
    }

    fig_assessment = create_assessment_radar(sample_assessment)
    if fig_assessment:
        st.plotly_chart(fig_assessment, use_container_width=True)


def display_problem_assessment():
    """Display problem assessment visualizations."""
    st.subheader("🔍 Problem Assessment")

    sample_problems = [
        {"name": "Acute Pain", "severity": 8},
        {"name": "Limited Mobility", "severity": 6},
        {"name": "Risk of Falls", "severity": 7},
        {"name": "Impaired Nutrition", "severity": 5},
        {"name": "Sleep Disturbance", "severity": 6}
    ]

    fig_severity = create_problem_severity_chart(sample_problems)
    if fig_severity:
        st.plotly_chart(fig_severity, use_container_width=True)


def display_intervention_analysis():
    """Display intervention effectiveness analysis."""
    st.subheader("💊 Intervention Analysis")

    sample_interventions = [
        {
            "intervention": "Pain Medication",
            "duration_days": 7,
            "effectiveness": 8.5,
            "patient_benefit": 85,
            "category": "Pharmacological"
        },
        {
            "intervention": "Physical Therapy",
            "duration_days": 14,
            "effectiveness": 7.2,
            "patient_benefit": 72,
            "category": "Rehabilitation"
        },
        {
            "intervention": "Nutritional Support",
            "duration_days": 10,
            "effectiveness": 6.8,
            "patient_benefit": 68,
            "category": "Supportive Care"
        },
        {
            "intervention": "Patient Education",
            "duration_days": 5,
            "effectiveness": 7.9,
            "patient_benefit": 79,
            "category": "Educational"
        }
    ]

    fig_interventions = create_intervention_effectiveness_chart(
        sample_interventions
    )
    if fig_interventions:
        st.plotly_chart(fig_interventions, use_container_width=True)


def display_health_indicators():
    """Display health indicators with gauges."""
    st.subheader("📊 Health Indicators")

    col1, col2, col3 = st.columns(3)

    indicators = [
        ("Blood Pressure", 78, 80),
        ("Oxygen Saturation", 96, 95),
        ("Pain Score", 35, 30)
    ]

    for idx, (name, current, target) in enumerate(indicators):
        with st.columns(3)[idx % 3]:
            fig = create_health_indicators_gauge(name, current, target)
            st.plotly_chart(fig, use_container_width=True)


if __name__ == "__main__":
    st.set_page_config(page_title="Nursing Visualizations")
    st.title("🏥 Nursing Care Plan Visualizations")

    page = st.sidebar.radio(
        "Select View",
        ["Care Plan Dashboard", "Problem Assessment", "Intervention Analysis",
         "Health Indicators"]
    )

    if page == "Care Plan Dashboard":
        display_care_plan_dashboard()
    elif page == "Problem Assessment":
        display_problem_assessment()
    elif page == "Intervention Analysis":
        display_intervention_analysis()
    elif page == "Health Indicators":
        display_health_indicators()
