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
COPY --chown=nursing:nursing app.py .
COPY --chown=nursing:nursing visualizations.py .
COPY --chown=nursing:nursing harvest_fons.py .
COPY --chown=nursing:nursing ingest_fast.py .
COPY --chown=nursing:nursing chroma_db_fons ./chroma_db_fons

# Create .streamlit config directory
RUN mkdir -p /app/.streamlit

# Streamlit configuration for production
RUN cat > /app/.streamlit/config.toml << 'EOF'
[theme]
primaryColor = "#FF6B6B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
font = "sans serif"

[server]
port = 8501
address = 0.0.0.0
maxUploadSize = 200
enableXsrfProtection = true
enableCORS = false
headless = true
runOnSave = false

[client]
showErrorDetails = false
showWarningOnDirectExecution = false

[logger]
level = "info"

[browser]
gatherUsageStats = false
EOF

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD curl -f http://localhost:8501/health || exit 1

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
CMD ["streamlit", "run", "app.py", "--logger.level=info"]
