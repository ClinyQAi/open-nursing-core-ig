# Azure Deployment Script for NHS Nursing Validator Phase 3 - PowerShell Version
# Run this script in PowerShell (as Administrator)

Write-Host "=== NHS Nursing Validator Phase 3 - Azure Deployment ===" -ForegroundColor Yellow
Write-Host ""

# Configuration
$RESOURCE_GROUP = "nursing-validator-prod"
$LOCATION = "uksouth"
$CONTAINER_REGISTRY = "nursingvalidatoracr"
$APP_NAME = "nursing-validator"
$IMAGE_NAME = "nursing-validator:latest"

Write-Host "Configuration:" -ForegroundColor Cyan
Write-Host "  Resource Group: $RESOURCE_GROUP"
Write-Host "  Location: $LOCATION"
Write-Host "  Container Registry: $CONTAINER_REGISTRY"
Write-Host "  App Name: $APP_NAME"
Write-Host ""

# Step 1: Check Azure CLI
Write-Host "Step 1: Checking Azure CLI..." -ForegroundColor Cyan
try {
    az --version | Out-Null
    Write-Host "✓ Azure CLI found" -ForegroundColor Green
} catch {
    Write-Host "✗ Azure CLI not found. Install from: https://learn.microsoft.com/en-us/cli/azure/install-azure-cli" -ForegroundColor Red
    exit 1
}

# Step 2: Check Docker
Write-Host ""
Write-Host "Step 2: Checking Docker..." -ForegroundColor Cyan
try {
    docker --version | Out-Null
    Write-Host "✓ Docker found" -ForegroundColor Green
} catch {
    Write-Host "✗ Docker not found. Please install Docker Desktop" -ForegroundColor Red
    exit 1
}

# Step 3: Check for .env.production
Write-Host ""
Write-Host "Step 3: Checking configuration..." -ForegroundColor Cyan
if (-Not (Test-Path ".env.production")) {
    Write-Host "✗ .env.production not found" -ForegroundColor Red
    exit 1
}
Write-Host "✓ .env.production found" -ForegroundColor Green

# Step 4: Create resource group
Write-Host ""
Write-Host "Step 4: Creating resource group..." -ForegroundColor Cyan
az group create --name $RESOURCE_GROUP --location $LOCATION
Write-Host "✓ Resource group created" -ForegroundColor Green

# Step 5: Create container registry
Write-Host ""
Write-Host "Step 5: Creating container registry..." -ForegroundColor Cyan
az acr create --resource-group $RESOURCE_GROUP --name $CONTAINER_REGISTRY --sku Basic
Write-Host "✓ Container registry created" -ForegroundColor Green

# Step 6: Build Docker image
Write-Host ""
Write-Host "Step 6: Building Docker image (this may take 3-5 minutes)..." -ForegroundColor Cyan
az acr build --registry $CONTAINER_REGISTRY --image $IMAGE_NAME --file Dockerfile .
Write-Host "✓ Docker image built and pushed" -ForegroundColor Green

# Step 7: Get registry credentials
Write-Host ""
Write-Host "Step 7: Getting registry credentials..." -ForegroundColor Cyan
$REGISTRY_URL = "$CONTAINER_REGISTRY.azurecr.io"
$REGISTRY_USERNAME = az acr credential show --name $CONTAINER_REGISTRY --query username --output tsv
$REGISTRY_PASSWORD = az acr credential show --name $CONTAINER_REGISTRY --query "passwords[0].value" --output tsv
Write-Host "✓ Registry credentials retrieved" -ForegroundColor Green

# Step 8: Read environment variables
Write-Host ""
Write-Host "Step 8: Reading environment configuration..." -ForegroundColor Cyan
$ENV_VARS = @{}
Get-Content .env.production | ForEach-Object {
    if ($_ -match '^([^=]+)=(.*)$') {
        $ENV_VARS[$matches[1]] = $matches[2]
    }
}
Write-Host "✓ Environment variables loaded" -ForegroundColor Green

# Step 9: Deploy to Container Instances
Write-Host ""
Write-Host "Step 9: Deploying to Azure Container Instances (this may take 2-3 minutes)..." -ForegroundColor Cyan
Write-Host "        Please be patient, deployment is in progress..." -ForegroundColor Yellow

az container create `
    --resource-group $RESOURCE_GROUP `
    --name $APP_NAME `
    --image "$REGISTRY_URL/$IMAGE_NAME" `
    --registry-login-server $REGISTRY_URL `
    --registry-username $REGISTRY_USERNAME `
    --registry-password $REGISTRY_PASSWORD `
    --cpu 2 `
    --memory 4 `
    --ports 8501 `
    --environment-variables `
        APP_ENV=production `
        LOG_LEVEL=info `
    --secure-environment-variables `
        AZURE_OPENAI_ENDPOINT=$($ENV_VARS['AZURE_OPENAI_ENDPOINT']) `
        AZURE_OPENAI_API_KEY=$($ENV_VARS['AZURE_OPENAI_API_KEY']) `
        AZURE_OPENAI_API_VERSION=$($ENV_VARS['AZURE_OPENAI_API_VERSION']) `
        AZURE_OPENAI_DEPLOYMENT=$($ENV_VARS['AZURE_OPENAI_DEPLOYMENT']) `
    --restart-policy OnFailure

Write-Host "✓ Deployment initiated" -ForegroundColor Green

# Step 10: Get container details
Write-Host ""
Write-Host "Step 10: Getting container details..." -ForegroundColor Cyan
az container show `
    --resource-group $RESOURCE_GROUP `
    --name $APP_NAME `
    --query "{ FQDN: ipAddress.fqdn, State: containers[0].instanceView.currentState.state, CPU: containers[0].resources.requests.cpu, Memory: containers[0].resources.requests.memoryInGb }" `
    --output table

# Step 11: Get FQDN and display final message
Write-Host ""
Write-Host "Step 11: Retrieving public URL..." -ForegroundColor Cyan
$FQDN = az container show --resource-group $RESOURCE_GROUP --name $APP_NAME --query ipAddress.fqdn --output tsv

Write-Host ""
Write-Host "✅ Deployment Complete!" -ForegroundColor Green
Write-Host ""
Write-Host "Access your application at:" -ForegroundColor Green
Write-Host "  http://$($FQDN):8501" -ForegroundColor Cyan
Write-Host ""
Write-Host "Login credentials:" -ForegroundColor Green
Write-Host "  Username: admin" -ForegroundColor Cyan
Write-Host "  Password: admin2025" -ForegroundColor Cyan
Write-Host ""
Write-Host "Monitor deployment:" -ForegroundColor Green
Write-Host "  az container logs --resource-group $RESOURCE_GROUP --name $APP_NAME" -ForegroundColor Cyan
Write-Host ""
Write-Host "View metrics:" -ForegroundColor Green
Write-Host "  az container show --resource-group $RESOURCE_GROUP --name $APP_NAME" -ForegroundColor Cyan
Write-Host ""
