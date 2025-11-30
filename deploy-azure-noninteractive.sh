#!/bin/bash
# Azure Deployment Script for NHS Nursing Validator Phase 3 (Non-interactive)

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}=== NHS Nursing Validator Phase 3 - Azure Deployment (Non-interactive) ===${NC}"
echo ""

# Configuration
RESOURCE_GROUP="nursing-validator-prod"
LOCATION="uksouth"
CONTAINER_REGISTRY="nursingvalidatoracr"
APP_NAME="nursing-validator"
IMAGE_NAME="nursing-validator:latest"

# Check prerequisites
echo "Checking prerequisites..."
command -v az >/dev/null 2>&1 || { echo -e "${RED}❌ Azure CLI not installed${NC}"; exit 1; }
echo -e "${GREEN}✓ Azure CLI installed${NC}"

# Check if already authenticated
echo ""
echo "Checking Azure authentication..."
ACCOUNT=$(az account show 2>/dev/null || true)
if [ -z "$ACCOUNT" ]; then
  echo -e "${YELLOW}⚠ Not authenticated with Azure${NC}"
  echo "Please run: az login --use-device-code"
  echo "Then re-run this script."
  exit 1
fi
echo -e "${GREEN}✓ Already authenticated with Azure${NC}"

# Check if resource group exists
echo ""
echo "Checking resource group: $RESOURCE_GROUP"
if ! az group exists --name $RESOURCE_GROUP | grep -q true; then
  echo "Creating resource group: $RESOURCE_GROUP"
  az group create \
    --name $RESOURCE_GROUP \
    --location $LOCATION
  echo -e "${GREEN}✓ Resource group created${NC}"
else
  echo -e "${GREEN}✓ Resource group exists${NC}"
fi

# Check if container registry exists
echo ""
echo "Checking container registry: $CONTAINER_REGISTRY"
if ! az acr show --name $CONTAINER_REGISTRY --resource-group $RESOURCE_GROUP &>/dev/null; then
  echo "Creating container registry: $CONTAINER_REGISTRY"
  az acr create \
    --resource-group $RESOURCE_GROUP \
    --name $CONTAINER_REGISTRY \
    --sku Basic
  echo -e "${GREEN}✓ Container registry created${NC}"
else
  echo -e "${GREEN}✓ Container registry exists${NC}"
fi

# Build Docker image
echo ""
echo "Building Docker image..."
az acr build \
  --registry $CONTAINER_REGISTRY \
  --image $IMAGE_NAME \
  --file Dockerfile .
echo -e "${GREEN}✓ Docker image built and pushed${NC}"

# Get registry credentials
REGISTRY_URL="${CONTAINER_REGISTRY}.azurecr.io"
REGISTRY_USERNAME=$(az acr credential show --name $CONTAINER_REGISTRY --query username --output tsv)
REGISTRY_PASSWORD=$(az acr credential show --name $CONTAINER_REGISTRY --query passwords[0].value --output tsv)

# Deploy to Container Instances
echo ""
echo "Deploying to Azure Container Instances..."

# Read environment variables from .env.production
if [ ! -f ".env.production" ]; then
  echo -e "${RED}❌ .env.production not found${NC}"
  exit 1
fi

# Check if container already exists
if az container show --resource-group $RESOURCE_GROUP --name $APP_NAME &>/dev/null; then
  echo "Deleting existing container: $APP_NAME"
  az container delete \
    --resource-group $RESOURCE_GROUP \
    --name $APP_NAME \
    --yes
  sleep 5
fi

az container create \
  --resource-group $RESOURCE_GROUP \
  --name $APP_NAME \
  --image "$REGISTRY_URL/$IMAGE_NAME" \
  --registry-login-server $REGISTRY_URL \
  --registry-username $REGISTRY_USERNAME \
  --registry-password $REGISTRY_PASSWORD \
  --cpu 2 \
  --memory 4 \
  --ports 8501 \
  --environment-variables \
    APP_ENV=production \
    LOG_LEVEL=info \
  --secure-environment-variables \
    AZURE_OPENAI_ENDPOINT="$(grep AZURE_OPENAI_ENDPOINT .env.production | cut -d '=' -f 2)" \
    AZURE_OPENAI_API_KEY="$(grep AZURE_OPENAI_API_KEY .env.production | cut -d '=' -f 2)" \
    AZURE_OPENAI_API_VERSION="$(grep AZURE_OPENAI_API_VERSION .env.production | cut -d '=' -f 2)" \
    AZURE_OPENAI_DEPLOYMENT="$(grep AZURE_OPENAI_DEPLOYMENT .env.production | cut -d '=' -f 2)" \
  --restart-policy OnFailure

echo -e "${GREEN}✓ Deployment initiated${NC}"

# Wait a bit for container to start
echo ""
echo "Waiting for container to start..."
sleep 10

# Get container details
echo ""
echo "Container Details:"
az container show \
  --resource-group $RESOURCE_GROUP \
  --name $APP_NAME \
  --query "{ FQDN: ipAddress.fqdn, State: containers[0].instanceView.currentState.state, CPU: containers[0].resources.requests.cpu, Memory: containers[0].resources.requests.memoryInGb }" \
  --output table

# Get FQDN
FQDN=$(az container show --resource-group $RESOURCE_GROUP --name $APP_NAME --query ipAddress.fqdn --output tsv)

echo ""
echo -e "${GREEN}✅ Deployment Complete!${NC}"
echo ""
echo "Access your application at:"
echo -e "${GREEN}http://$FQDN:8501${NC}"
echo ""
echo "Monitor deployment:"
echo "  az container logs --resource-group $RESOURCE_GROUP --name $APP_NAME"
echo ""
echo "View metrics:"
echo "  az container show --resource-group $RESOURCE_GROUP --name $APP_NAME"
