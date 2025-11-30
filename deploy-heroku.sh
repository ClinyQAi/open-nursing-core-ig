#!/bin/bash
# Heroku Deployment Script for NHS Nursing Validator Phase 3

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}=== NHS Nursing Validator Phase 3 - Heroku Deployment ===${NC}"
echo ""

# Configuration
APP_NAME="nursing-validator"

# Check prerequisites
echo "Checking prerequisites..."
command -v heroku >/dev/null 2>&1 || { echo -e "${RED}❌ Heroku CLI not installed${NC}"; exit 1; }
command -v git >/dev/null 2>&1 || { echo -e "${RED}❌ Git not installed${NC}"; exit 1; }
echo -e "${GREEN}✓ Prerequisites installed${NC}"

# Login to Heroku
echo ""
echo "Logging in to Heroku..."
heroku login

# Check if app exists
echo ""
echo "Checking app existence..."
if heroku apps:info --app $APP_NAME > /dev/null 2>&1; then
  echo -e "${GREEN}✓ App exists: $APP_NAME${NC}"
else
  echo "Creating new Heroku app: $APP_NAME"
  heroku create $APP_NAME
  echo -e "${GREEN}✓ App created${NC}"
fi

# Add buildpack
echo ""
echo "Configuring buildpacks..."
heroku buildpacks:clear --app $APP_NAME || true
heroku buildpacks:add heroku/python --app $APP_NAME
echo -e "${GREEN}✓ Buildpacks configured${NC}"

# Set environment variables
echo ""
echo "Setting environment variables..."

if [ ! -f ".env.production" ]; then
  echo -e "${RED}❌ .env.production not found${NC}"
  exit 1
fi

# Extract variables and set them
AZURE_OPENAI_ENDPOINT=$(grep AZURE_OPENAI_ENDPOINT .env.production | cut -d '=' -f 2-)
AZURE_OPENAI_API_KEY=$(grep AZURE_OPENAI_API_KEY .env.production | cut -d '=' -f 2-)
AZURE_OPENAI_API_VERSION=$(grep AZURE_OPENAI_API_VERSION .env.production | cut -d '=' -f 2-)
AZURE_OPENAI_DEPLOYMENT=$(grep AZURE_OPENAI_DEPLOYMENT .env.production | cut -d '=' -f 2-)

heroku config:set \
  --app $APP_NAME \
  APP_ENV=production \
  LOG_LEVEL=info \
  AZURE_OPENAI_ENDPOINT="$AZURE_OPENAI_ENDPOINT" \
  AZURE_OPENAI_API_KEY="$AZURE_OPENAI_API_KEY" \
  AZURE_OPENAI_API_VERSION="$AZURE_OPENAI_API_VERSION" \
  AZURE_OPENAI_DEPLOYMENT="$AZURE_OPENAI_DEPLOYMENT"

echo -e "${GREEN}✓ Environment variables set${NC}"

# Create Procfile
echo ""
echo "Creating Procfile..."
cat > Procfile << 'EOF'
web: streamlit run app_phase2.py --server.port=$PORT --server.address=0.0.0.0
EOF
echo -e "${GREEN}✓ Procfile created${NC}"

# Add Heroku remote if not exists
echo ""
echo "Adding Heroku remote..."
git remote remove heroku || true
heroku git:remote --app $APP_NAME

# Deploy
echo ""
echo "Deploying to Heroku..."
git push heroku main

echo ""
echo -e "${GREEN}✅ Deployment Complete!${NC}"
echo ""

# Get app URL
APP_URL=$(heroku apps:info --app $APP_NAME --json | grep -o '"web_url":"[^"]*' | cut -d'"' -f4)

echo "Access your application at:"
echo -e "${GREEN}$APP_URL${NC}"
echo ""
echo "Monitor deployment:"
echo "  heroku logs --tail --app $APP_NAME"
echo ""
echo "View app info:"
echo "  heroku apps:info --app $APP_NAME"
