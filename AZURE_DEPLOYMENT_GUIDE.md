# Azure Deployment Guide for NHS Nursing Validator Phase 3

## Overview

This guide provides multiple deployment options for the NHS Nursing Validator Phase 3 application on Azure.

## Option 1: GitHub Actions Deployment (Recommended)

GitHub Actions provides a secure, automated way to deploy to Azure without needing to log in locally.

### Prerequisites

1. **Azure Credentials**: You need a Service Principal for authentication
   - If you don't have one, create it using:
     ```bash
     az ad sp create-for-rbac --name "NursingValidator" --role Contributor --scopes /subscriptions/{SUBSCRIPTION_ID}
     ```

2. **GitHub Secrets**: Add these to your GitHub repository settings (Settings → Secrets and variables → Actions):
   - `AZURE_CREDENTIALS`: The entire JSON output from the service principal creation (in format shown below)
   - `AZURE_OPENAI_ENDPOINT`: Your Azure OpenAI endpoint URL
   - `AZURE_OPENAI_API_KEY`: Your Azure OpenAI API key
   - `AZURE_OPENAI_DEPLOYMENT`: Your deployment name (e.g., "gpt-4o")
   - `AZURE_OPENAI_API_VERSION`: API version (e.g., "2024-08-01-preview")

### AZURE_CREDENTIALS Format

The `AZURE_CREDENTIALS` secret should be a JSON object:
```json
{
  "clientId": "...",
  "clientSecret": "...",
  "subscriptionId": "...",
  "tenantId": "..."
}
```

### Deployment Steps

1. Go to GitHub repository
2. Navigate to **Actions** tab
3. Click on **"Deploy to Azure"** workflow
4. Click **"Run workflow"**
5. Optionally select **"production"** or **"staging"** environment
6. Wait for deployment to complete
7. The deployment URL will be displayed in the workflow logs

---

## Option 2: Local Deployment (Testing)

For local testing and development:

```bash
# Install dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Set environment variables
export $(cat .env.production | xargs)

# Run the application
streamlit run app_phase2.py
```

Access at: `http://localhost:8501`

---

## Option 3: Manual Azure CLI Deployment

For direct deployment using Azure CLI (requires authentication):

### Prerequisites

1. Install Azure CLI: https://learn.microsoft.com/en-us/cli/azure/install-azure-cli
2. Authenticate: `az login --use-device-code`
3. Create `.env.production` file with your credentials (see template below)

### Environment Configuration

Create `.env.production`:

```bash
# Production Environment Configuration for NHS Nursing Validator - Azure Deployment

# ============================================
# AZURE OPENAI CONFIGURATION (REQUIRED)
# ============================================
AZURE_OPENAI_ENDPOINT=https://{resource-name}.openai.azure.com/
AZURE_OPENAI_API_KEY={your-api-key}
AZURE_OPENAI_API_VERSION=2024-08-01-preview
AZURE_OPENAI_DEPLOYMENT=gpt-4o

# ============================================
# APPLICATION SETTINGS
# ============================================
APP_ENV=production
APP_NAME=NHS Nursing Validator
LOG_LEVEL=info
DEBUG=false
USE_DATABASE=false

# ============================================
# SECURITY SETTINGS
# ============================================
ENABLE_AUTHENTICATION=true
SESSION_TIMEOUT_MINUTES=30
MAX_LOGIN_ATTEMPTS=5
LOGIN_ATTEMPT_COOLDOWN_SECONDS=300

# ============================================
# STORAGE CONFIGURATION
# ============================================
STORAGE_TYPE=local

# ============================================
# LOGGING CONFIGURATION
# ============================================
LOG_FORMAT=json
LOG_FILE=/app/logs/app.log
LOG_MAX_SIZE_MB=100
LOG_BACKUP_COUNT=10

# ============================================
# STREAMLIT SPECIFIC
# ============================================
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_SERVER_ENABLE_CORS=false
STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION=true
STREAMLIT_CLIENT_SHOW_ERROR_DETAILS=false
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
```

### Deployment Command

```bash
# Using the non-interactive deployment script (if already authenticated)
bash deploy-azure-noninteractive.sh

# Or step-by-step:
az login --use-device-code

# Build and deploy
az acr build \
  --registry nursingvalidatoracr \
  --image nursing-validator:latest \
  --file Dockerfile .

az container create \
  --resource-group nursing-validator-prod \
  --name nursing-validator \
  --image nursingvalidatoracr.azurecr.io/nursing-validator:latest \
  --cpu 2 \
  --memory 4 \
  --ports 8501 \
  --restart-policy OnFailure
```

---

## Option 4: Docker Local Deployment

For testing the Docker image locally:

```bash
# Build the image
docker build -t nursing-validator:latest .

# Run the container
docker run -p 8501:8501 \
  -e AZURE_OPENAI_ENDPOINT=${AZURE_OPENAI_ENDPOINT} \
  -e AZURE_OPENAI_API_KEY=${AZURE_OPENAI_API_KEY} \
  -e AZURE_OPENAI_DEPLOYMENT=${AZURE_OPENAI_DEPLOYMENT} \
  -e AZURE_OPENAI_API_VERSION=${AZURE_OPENAI_API_VERSION} \
  nursing-validator:latest
```

Access at: `http://localhost:8501`

---

## Application Access

### Login Credentials

- **Username**: `admin`
- **Password**: `admin2025`

### Features Available

1. **Predictions Dashboard**: ML-powered problem predictions
2. **Recommendations Dashboard**: Context-aware clinical recommendations
3. **Anomaly Detection**: Identify unusual patterns in data
4. **Explainability**: SHAP values for model interpretability

---

## Monitoring & Logs

### View Container Logs

```bash
az container logs \
  --resource-group nursing-validator-prod \
  --name nursing-validator
```

### View Container Status

```bash
az container show \
  --resource-group nursing-validator-prod \
  --name nursing-validator
```

### Stream Logs Live

```bash
az container attach \
  --resource-group nursing-validator-prod \
  --name nursing-validator
```

---

## Troubleshooting

### Azure CLI Authentication Issues

If you encounter "JSON is invalid" errors:

1. Update Azure CLI: `pip install --upgrade azure-cli`
2. Try clearing cache: `rm -rf ~/.azure`
3. Use device code: `az login --use-device-code`

### Container Build Failures

If Docker build fails due to dependency conflicts:

1. Check `requirements.txt` for version incompatibilities
2. Update individual packages as needed
3. Test locally first: `docker build -t test:latest .`

### Application Not Responding

1. Check container is running: `az container show --resource-group nursing-validator-prod --name nursing-validator`
2. View logs for errors: `az container logs --resource-group nursing-validator-prod --name nursing-validator`
3. Verify AZURE_OPENAI credentials are correct

---

## Deployment Architecture

```
┌─────────────────────────────────────────────────────┐
│         NHS Nursing Validator Phase 3                │
├─────────────────────────────────────────────────────┤
│  Streamlit Frontend (Port 8501)                      │
│  ├─ Predictions Dashboard                           │
│  ├─ Recommendations Dashboard                       │
│  ├─ Anomaly Detection Dashboard                     │
│  └─ Explainability Dashboard                        │
├─────────────────────────────────────────────────────┤
│  ML Models & Services                               │
│  ├─ scikit-learn (Predictions)                      │
│  ├─ LangChain + ChromaDB (Recommendations)          │
│  ├─ Isolation Forest (Anomaly Detection)            │
│  └─ SHAP (Explainability)                           │
├─────────────────────────────────────────────────────┤
│  Azure Services                                      │
│  ├─ Azure Container Registry (Image Storage)        │
│  ├─ Azure Container Instances (Runtime)             │
│  └─ Azure OpenAI (GPT-4o Access)                    │
└─────────────────────────────────────────────────────┘
```

---

## Next Steps

1. **Choose a deployment option** from above
2. **Gather required credentials**:
   - Azure Subscription ID
   - Azure OpenAI credentials
   - Service Principal (for GitHub Actions)
3. **Execute deployment**
4. **Verify access** at the provided URL
5. **Test functionality** with sample data
6. **Set up monitoring** and alerts

---

## Support & Troubleshooting

For issues or questions:

1. Check the application logs: `az container logs --resource-group nursing-validator-prod --name nursing-validator`
2. Review GitHub Actions workflow logs: Repository → Actions → Workflow run details
3. Verify all environment variables are set correctly
4. Ensure Azure resources exist in the correct subscription

---

**Last Updated**: November 30, 2025  
**Application Version**: Phase 3  
**Deployment Status**: Ready for Azure deployment via GitHub Actions (Recommended)
