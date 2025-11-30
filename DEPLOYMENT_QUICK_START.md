# 🚀 Quick Start: Deploy Now

## ✅ All Azure Credentials Ready!

You have all the credentials needed for deployment. Choose your method:

---

## **Method 1: Manual Setup (2 minutes)** ⭐ EASIEST

1. Open GitHub: https://github.com/ClinyQAi/open-nursing-core-ig/settings/secrets/actions

2. Add these 6 secrets by clicking "New repository secret":

| Secret Name | Value |
|------------|-------|
| `AZURE_CLIENT_ID` | *Your Client ID from credentials* |
| `AZURE_CLIENT_SECRET` | *Your Client Secret from credentials* |
| `AZURE_TENANT_ID` | *Your Tenant ID from credentials* |
| `AZURE_SUBSCRIPTION_ID` | *Your Subscription ID from credentials* |
| `AZURE_OPENAI_ENDPOINT` | *Your Azure OpenAI Endpoint* |
| `AZURE_OPENAI_API_KEY` | *Your Azure OpenAI API Key* |

3. Go to: https://github.com/ClinyQAi/open-nursing-core-ig/actions

4. Click **"Deploy to Azure"** workflow

5. Click **"Run workflow"**

6. ⏳ Wait 5-10 minutes

7. ✅ Check the workflow logs for your deployment URL!

---

## **Method 2: Automated Setup (requires GitHub CLI)**

If you have `gh` CLI installed:

```bash
cd /path/to/open-nursing-core-ig
bash github-secrets-setup.sh
```

Then go to Actions and run the workflow.

---

## **Method 3: Local Deployment (Your Machine)**

If you prefer to deploy from your local machine:

```bash
# On your local machine with Azure CLI installed
git clone https://github.com/ClinyQAi/open-nursing-core-ig.git
cd open-nursing-core-ig

# Create .env.production
cat > .env.production << 'EOF'
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=your-api-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
AZURE_OPENAI_DEPLOYMENT=gpt-4o
APP_ENV=production
LOG_LEVEL=info
ENABLE_AUTHENTICATION=true
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
EOF

# Authenticate with Azure
az login --service-principal \
  -u YOUR_CLIENT_ID \
  -p 'YOUR_CLIENT_SECRET' \
  --tenant YOUR_TENANT_ID

az account set --subscription YOUR_SUBSCRIPTION_ID

# Deploy
bash deploy-azure.sh
```

---

## **What You'll Get**

After deployment completes:

✅ **Public URL** (example):
```
http://nursing-validator.uksouth.azurecontainers.io:8501
```

✅ **Login Credentials**:
- Username: `admin`
- Password: `admin2025`

✅ **Features**:
- Predictions Dashboard (ML predictions)
- Recommendations Dashboard (Clinical recommendations)
- Anomaly Detection (Pattern detection)
- Explainability (SHAP-based interpretability)

---

## **Timeline**

| Step | Duration |
|------|----------|
| Setup Secrets | 2 min |
| GitHub Workflow Running | 5-10 min |
| **Total** | **7-12 min** |

---

## **Deployment Infrastructure**

- **Location**: UK South (uksouth)
- **CPU**: 2 cores
- **Memory**: 4 GB RAM
- **Port**: 8501 (Streamlit)
- **Registry**: Azure Container Registry
- **Runtime**: Azure Container Instances
- **AI**: Azure OpenAI (GPT-4o)

---

## **After Deployment**

### Monitor Your Application

```bash
# View logs
az container logs --resource-group nursing-validator-prod --name nursing-validator

# Check status
az container show --resource-group nursing-validator-prod --name nursing-validator

# Get public IP
az container show --resource-group nursing-validator-prod --name nursing-validator --query ipAddress.fqdn
```

### Stop/Delete

```bash
# Stop container
az container stop --resource-group nursing-validator-prod --name nursing-validator

# Delete everything
az group delete --resource-group nursing-validator-prod --yes
```

---

## **Troubleshooting**

| Issue | Solution |
|-------|----------|
| GitHub Actions fails with auth error | Check all 6 secrets are added correctly (no extra spaces) |
| Container doesn't start | Check logs: `az container logs --resource-group nursing-validator-prod --name nursing-validator` |
| Public IP not assigned | Wait 30 seconds and check again, Azure takes time to allocate IPs |
| Can't access the URL | Check firewall allows port 8501, or wait for container to fully start |

---

## **Quick Links**

- 📚 **Full Deployment Guide**: `AZURE_DEPLOYMENT_GUIDE.md`
- 🔐 **Credentials Setup**: `AZURE_CREDENTIALS_SETUP.md`
- 📋 **Deployment Checklist**: `DEPLOYMENT_READY.md`
- 🔧 **GitHub Secrets Setup Script**: `github-secrets-setup.sh`

---

## **NEXT STEP: Choose Method 1, 2, or 3 above and proceed!** 🎯

**Recommended**: Method 1 (Manual Setup) - Takes only 2 minutes!
