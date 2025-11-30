# Production-Grade Multi-Stage Dockerfile
# Stage 1: Builder
FROM python:3.11-slim as builder

WORKDIR /build

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Create wheel files for faster deployment
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /build/wheels -r requirements.txt

# Stage 2: Runtime
FROM python:3.11-slim

WORKDIR /app

# Create non-root user for security
RUN useradd -m -u 1000 nursing && \
    mkdir -p /app /app/data /app/logs && \
    chown -R nursing:nursing /app

# Install runtime dependencies only
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Copy wheels from builder
COPY --from=builder /build/wheels /wheels
COPY --from=builder /build/requirements.txt .

# Install Python packages from wheels
RUN pip install --no-cache /wheels/*

# Switch to non-root user
USER nursing

# Copy application code
COPY --chown=nursing:nursing app_phase2.py .
COPY --chown=nursing:nursing database.py .
COPY --chown=nursing:nursing db_migrations.py .
COPY --chown=nursing:nursing ml_*.py .
COPY --chown=nursing:nursing visualizations.py .
COPY --chown=nursing:nursing harvest_fons.py .
COPY --chown=nursing:nursing ingest_fast.py .
COPY --chown=nursing:nursing chroma_db_fons ./chroma_db_fons

# Create .streamlit config directory
RUN mkdir -p /app/.streamlit

# Streamlit configuration for production
RUN mkdir -p /app/.streamlit

# Write config.toml
RUN echo '[theme]' > /app/.streamlit/config.toml && \
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

# Set environment variables for production
ENV STREAMLIT_SERVER_HEADLESS=true \
    STREAMLIT_SERVER_ENABLE_CORS=false \
    STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION=true \
    STREAMLIT_CLIENT_SHOW_ERROR_DETAILS=false \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Run application
CMD ["streamlit", "run", "app_phase2.py", "--logger.level=info"]
