#!/bin/bash
# Quick deployment launcher for NHS Nursing Validator Phase 3
# Run this on your LOCAL machine (not in the dev container)

echo "=========================================="
echo "NHS Nursing Validator Phase 3"
echo "Azure Deployment Launcher"
echo "=========================================="
echo ""
echo "This script will guide you through deploying to Azure."
echo ""

# Check if we're in the project directory
if [ ! -f "deploy-azure.sh" ]; then
  echo "❌ Error: deploy-azure.sh not found in current directory"
  echo ""
  echo "Please:"
  echo "1. Clone/navigate to the project repository"
  echo "2. Run: git pull origin main"
  echo "3. Then run this script again"
  exit 1
fi

echo "✓ Project directory verified"
echo ""

# Check for .env.production
if [ ! -f ".env.production" ]; then
  echo "⚠️  .env.production not found"
  echo ""
  echo "Creating template .env.production..."
  cat > .env.production << 'EOF'
# Production Environment Configuration for NHS Nursing Validator - Azure Deployment
# Generated: $(date)

# ============================================
# AZURE OPENAI CONFIGURATION (REQUIRED)
# ============================================
AZURE_OPENAI_ENDPOINT=https://{YOUR-RESOURCE}.openai.azure.com/
AZURE_OPENAI_API_KEY={YOUR-API-KEY}
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
EOF
  
  echo "✓ Template created at .env.production"
  echo ""
  echo "📝 Please edit .env.production and add:"
  echo "   - Your Azure OpenAI endpoint"
  echo "   - Your Azure OpenAI API key"
  echo ""
  echo "Then run this script again."
  exit 0
fi

echo "✓ .env.production found"
echo ""

# Check if .env.production has been configured
if grep -q "{YOUR-" .env.production; then
  echo "⚠️  .env.production needs configuration"
  echo ""
  echo "Please edit .env.production and replace:"
  echo "  - {YOUR-RESOURCE} with your Azure resource name"
  echo "  - {YOUR-API-KEY} with your Azure OpenAI API key"
  echo ""
  echo "Then run this script again."
  exit 0
fi

echo "✓ Credentials configured"
echo ""

# Check for Azure CLI
echo "Checking prerequisites..."
if ! command -v az &> /dev/null; then
  echo "❌ Azure CLI not found"
  echo ""
  echo "Please install Azure CLI:"
  echo "  https://learn.microsoft.com/en-us/cli/azure/install-azure-cli"
  exit 1
fi
echo "✓ Azure CLI installed"

# Check if Docker is available (optional but helpful)
if ! command -v docker &> /dev/null; then
  echo "⚠️  Docker not found (optional, used for building locally)"
else
  echo "✓ Docker installed"
fi

echo ""
echo "=========================================="
echo "Ready to Deploy!"
echo "=========================================="
echo ""

# Check Azure authentication
echo "Checking Azure authentication..."
if ! az account show &>/dev/null; then
  echo ""
  echo "⚠️  Not authenticated with Azure"
  echo ""
  echo "Running: az login --use-device-code"
  echo ""
  echo "Please:"
  echo "1. Open: https://microsoft.com/devicelogin"
  echo "2. Enter the code shown below"
  echo "3. Authenticate with your Azure account"
  echo ""
  
  az login --use-device-code
  
  if [ $? -ne 0 ]; then
    echo "❌ Authentication failed"
    exit 1
  fi
fi

ACCOUNT=$(az account show --query name -o tsv)
echo "✓ Authenticated as: $ACCOUNT"
echo ""

# Confirm before deploying
echo "=========================================="
echo "Deployment Summary"
echo "=========================================="
echo "Location: UK South (uksouth)"
echo "Container: nursing-validator"
echo "CPU: 2 cores"
echo "Memory: 4 GB"
echo "Port: 8501"
echo ""
read -p "Proceed with deployment? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
  echo "Deployment cancelled."
  exit 0
fi

echo ""
echo "Starting deployment..."
echo ""

# Run the deployment script
bash deploy-azure.sh

if [ $? -eq 0 ]; then
  echo ""
  echo "✅ Deployment completed successfully!"
  echo ""
  echo "To view logs:"
  echo "  az container logs --resource-group nursing-validator-prod --name nursing-validator"
  echo ""
  echo "To get the public URL:"
  echo "  az container show --resource-group nursing-validator-prod --name nursing-validator --query ipAddress.fqdn"
else
  echo ""
  echo "❌ Deployment failed"
  echo ""
  echo "For help, check:"
  echo "  - AZURE_DEPLOYMENT_GUIDE.md"
  echo "  - Container logs: az container logs --resource-group nursing-validator-prod --name nursing-validator"
  exit 1
fi
