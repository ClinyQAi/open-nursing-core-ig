#!/bin/bash
# GitHub Secrets Setup Helper for NHS Nursing Validator

echo "=========================================="
echo "GitHub Secrets Setup"
echo "=========================================="
echo ""
echo "This script will help you add your Azure credentials to GitHub."
echo ""

# Check if GitHub CLI is installed
if ! command -v gh &> /dev/null; then
  echo "⚠️  GitHub CLI (gh) not found"
  echo ""
  echo "Two options:"
  echo ""
  echo "OPTION 1: Install GitHub CLI and use this script"
  echo "  macOS: brew install gh"
  echo "  Linux: sudo apt-get install gh"
  echo "  Windows: choco install gh"
  echo "  Then run this script again: bash github-secrets-setup.sh"
  echo ""
  echo "OPTION 2: Add secrets manually on GitHub"
  echo "  Go to: https://github.com/ClinyQAi/open-nursing-core-ig/settings/secrets/actions"
  echo "  Click 'New repository secret' and add each secret below:"
  echo ""
  
  cat << 'EOF'
Secret 1:
  Name: AZURE_CLIENT_ID
  Value: [Your AZURE_CLIENT_ID]

Secret 2:
  Name: AZURE_CLIENT_SECRET
  Value: [Your AZURE_CLIENT_SECRET]

Secret 3:
  Name: AZURE_TENANT_ID
  Value: [Your AZURE_TENANT_ID]

Secret 4:
  Name: AZURE_SUBSCRIPTION_ID
  Value: [Your AZURE_SUBSCRIPTION_ID]

Secret 5:
  Name: AZURE_OPENAI_ENDPOINT
  Value: [Your AZURE_OPENAI_ENDPOINT]

Secret 6:
  Name: AZURE_OPENAI_API_KEY
  Value: [Your AZURE_OPENAI_API_KEY]

Secret 7 (Optional):
  Name: AZURE_OPENAI_DEPLOYMENT
  Value: gpt-4o

Secret 8 (Optional):
  Name: AZURE_OPENAI_API_VERSION
  Value: 2024-08-01-preview
EOF

  exit 0
fi

echo "GitHub CLI found! ✓"
echo ""

# Check if authenticated with GitHub
if ! gh auth status &>/dev/null; then
  echo "Authenticating with GitHub..."
  gh auth login
  echo ""
fi

REPO="ClinyQAi/open-nursing-core-ig"

echo "Adding secrets to $REPO..."
echo ""

# Add secrets - UPDATE THESE VALUES WITH YOUR ACTUAL CREDENTIALS
SECRETS=(
  "AZURE_CLIENT_ID:YOUR_CLIENT_ID"
  "AZURE_CLIENT_SECRET:YOUR_CLIENT_SECRET"
  "AZURE_TENANT_ID:YOUR_TENANT_ID"
  "AZURE_SUBSCRIPTION_ID:YOUR_SUBSCRIPTION_ID"
  "AZURE_OPENAI_ENDPOINT:YOUR_OPENAI_ENDPOINT"
  "AZURE_OPENAI_API_KEY:YOUR_OPENAI_API_KEY"
  "AZURE_OPENAI_DEPLOYMENT:gpt-4o"
  "AZURE_OPENAI_API_VERSION:2024-08-01-preview"
)

for secret in "${SECRETS[@]}"; do
  IFS=':' read -r NAME VALUE <<< "$secret"
  echo "Adding $NAME..."
  echo "$VALUE" | gh secret set "$NAME" --repo "$REPO"
  if [ $? -eq 0 ]; then
    echo "  ✓ $NAME added successfully"
  else
    echo "  ❌ Failed to add $NAME"
  fi
done

echo ""
echo "=========================================="
echo "✅ Secrets added successfully!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Go to: https://github.com/ClinyQAi/open-nursing-core-ig/actions"
echo "2. Click on 'Deploy to Azure' workflow"
echo "3. Click 'Run workflow'"
echo "4. Wait 5-10 minutes for deployment to complete"
echo ""
echo "Your application will be deployed to Azure! 🚀"
