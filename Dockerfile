# Production-Grade Dockerfile for NHS Nursing Validator Phase 3
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    ca-certificates \
    libssl-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create application directories
RUN mkdir -p /app/data /app/logs /app/.streamlit

# Copy application directories
COPY core/ /app/core/
COPY db/ /app/db/
COPY ml/ /app/ml/
COPY visualizations/ /app/visualizations/
COPY scripts/ /app/scripts/

# Copy application entry points
COPY app.py app_phase2.py .
COPY .env.example .

# Create Streamlit config
RUN mkdir -p /app/.streamlit && \
    echo '[theme]' > /app/.streamlit/config.toml && \
    echo 'primaryColor = "#FF6B6B"' >> /app/.streamlit/config.toml && \
    echo 'backgroundColor = "#FFFFFF"' >> /app/.streamlit/config.toml && \
    echo 'secondaryBackgroundColor = "#F0F2F6"' >> /app/.streamlit/config.toml && \
    echo 'font = "sans serif"' >> /app/.streamlit/config.toml && \
    echo '[server]' >> /app/.streamlit/config.toml && \
    echo 'port = 8501' >> /app/.streamlit/config.toml && \
    echo 'address = "0.0.0.0"' >> /app/.streamlit/config.toml && \
    echo 'maxUploadSize = 200' >> /app/.streamlit/config.toml && \
    echo 'enableXsrfProtection = true' >> /app/.streamlit/config.toml && \
    echo 'enableCORS = false' >> /app/.streamlit/config.toml && \
    echo 'headless = true' >> /app/.streamlit/config.toml && \
    echo 'runOnSave = false' >> /app/.streamlit/config.toml && \
    echo '[client]' >> /app/.streamlit/config.toml && \
    echo 'showErrorDetails = false' >> /app/.streamlit/config.toml && \
    echo 'showWarningOnDirectExecution = false' >> /app/.streamlit/config.toml && \
    echo '[logger]' >> /app/.streamlit/config.toml && \
    echo 'level = "info"' >> /app/.streamlit/config.toml && \
    echo '[browser]' >> /app/.streamlit/config.toml && \
    echo 'gatherUsageStats = false' >> /app/.streamlit/config.toml

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD curl -f http://localhost:8501/ || exit 1

# Expose port
EXPOSE 8501

# Environment variables
ENV STREAMLIT_SERVER_HEADLESS=true \
    STREAMLIT_SERVER_ENABLE_CORS=false \
    STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION=true \
    STREAMLIT_CLIENT_SHOW_ERROR_DETAILS=false \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Run application (default to phase 2)
CMD ["streamlit", "run", "app_phase2.py", "--logger.level=info"]
