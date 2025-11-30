# Azure Credentials Setup Guide

## Getting Your Azure Service Principal Credentials

To deploy via GitHub Actions, you need to create a Service Principal and add its credentials as GitHub Secrets.

### Step 1: Create Azure Service Principal

Run this command in your terminal (on your local machine with Azure CLI installed):

```bash
az ad sp create-for-rbac \
  --name "NursingValidatorDeploy" \
  --role Contributor \
  --scopes /subscriptions/{SUBSCRIPTION_ID}
```

Replace `{SUBSCRIPTION_ID}` with your actual Azure subscription ID.

**To find your subscription ID:**
```bash
az account list --query "[].{Name:name, ID:id}" --output table
```

### Step 2: Copy the Output

The command will output something like:

```json
{
  "appId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "displayName": "NursingValidatorDeploy",
  "password": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "tenant": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```

### Step 3: Add GitHub Secrets

Go to your GitHub repository:
1. **Settings** → **Secrets and variables** → **Actions**
2. Click **"New repository secret"**

Add these 6 secrets:

| Secret Name | Value |
|------------|-------|
| `AZURE_CLIENT_ID` | The `appId` from the output |
| `AZURE_CLIENT_SECRET` | The `password` from the output |
| `AZURE_TENANT_ID` | The `tenant` from the output |
| `AZURE_SUBSCRIPTION_ID` | Your subscription ID (from `az account list`) |
| `AZURE_OPENAI_ENDPOINT` | Your Azure OpenAI endpoint (e.g., `https://your-resource.openai.azure.com/`) |
| `AZURE_OPENAI_API_KEY` | Your Azure OpenAI API key |

**Optional (but recommended):**

| Secret Name | Value |
|------------|-------|
| `AZURE_OPENAI_DEPLOYMENT` | Your deployment name (default: `gpt-4o`) |
| `AZURE_OPENAI_API_VERSION` | API version (default: `2024-08-01-preview`) |

### Step 4: Verify Secrets Are Set

In your GitHub repository, go to **Settings** → **Secrets and variables** → **Actions** and confirm you see all 6 secrets listed.

### Step 5: Run Deployment

1. Go to your repository
2. Click **Actions** tab
3. Select **"Deploy to Azure"** workflow
4. Click **"Run workflow"**
5. The deployment will start automatically

---

## Finding Your Azure Credentials

### Azure Subscription ID
```bash
az account show --query id --output tsv
```

### Azure OpenAI Endpoint and API Key

1. Go to: https://portal.azure.com
2. Search for **"Azure OpenAI"**
3. Select your resource
4. Click **"Keys and Endpoint"** in the left sidebar
5. Copy:
   - **Endpoint**: (looks like `https://your-resource.openai.azure.com/`)
   - **Key 1** or **Key 2**: (your API key)

### Azure OpenAI Deployment Name

In the same Azure Portal resource:
1. Click **"Model deployments"** in the left sidebar
2. Look for your deployed model (usually shows something like `gpt-4o`)
3. The deployment name is shown in the list

---

## Troubleshooting

### "appId not found"
- Make sure you're logged into Azure: `az login`
- Check your subscription: `az account show`

### "Invalid subscription"
- Verify subscription ID: `az account list`
- Make sure it matches in the command

### "Insufficient permissions"
- The service principal needs **Contributor** role at minimum
- Contact your Azure subscription admin if you don't have permission to create service principals

### "GitHub Actions workflow fails with auth error"
- Verify all 6 secrets are present in GitHub
- Check spelling of secret names (case-sensitive)
- Ensure values don't have extra spaces or quotes

---

## Security Best Practices

1. **Never commit credentials** to your repository
2. **Rotate credentials regularly** in Azure (update GitHub Secrets accordingly)
3. **Use separate service principals** for different environments
4. **Limit permissions** - only give the minimum required roles
5. **Monitor usage** - check Azure activity logs regularly

---

## Quick Reference Commands

```bash
# List all subscriptions
az account list --query "[].{Name:name, ID:id}" --output table

# Show current subscription
az account show

# Create service principal
az ad sp create-for-rbac \
  --name "NursingValidatorDeploy" \
  --role Contributor \
  --scopes /subscriptions/{SUBSCRIPTION_ID}

# List service principals
az ad sp list --query "[].{Name:displayName, ID:appId}" --output table

# Get Azure OpenAI keys
az cognitiveservices account keys list --name {resource-name} --resource-group {resource-group}
```

---

## After Deployment

Once the GitHub Actions workflow completes successfully:

1. Go to GitHub repository → **Actions** → Select the completed workflow run
2. Scroll down to see the deployment URL
3. The URL will be something like: `http://nursing-validator.uksouth.azurecontainers.io:8501`
4. Open that URL in your browser
5. Login with:
   - **Username**: `admin`
   - **Password**: `admin2025`

---

**For more information**: https://github.com/Azure/login#readme
