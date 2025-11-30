# Azure Service Principal Issue - SOLUTION

## Problem

The service principal was created in the wrong Azure tenant ("Microsoft Accounts" instead of your actual tenant).

Error: `AADSTS700016: Application with identifier was not found in the directory 'Microsoft Accounts'`

## Solution

You need to create a NEW service principal in the CORRECT tenant. Here's how:

### Step 1: Find Your Correct Tenant ID

Run this command on your local machine:

```bash
az login
az account list --query "[].{Name:name, TenantId:tenantId, SubscriptionId:id}" --output table
```

Look for the row that matches your subscription. **Note the TenantId** - this is your CORRECT tenant ID.

### Step 2: Create Service Principal in Correct Tenant

```bash
# Replace {SUBSCRIPTION_ID} with your actual subscription ID from step 1
az ad sp create-for-rbac \
  --name "NursingValidatorServicePrincipal" \
  --role Contributor \
  --scopes /subscriptions/{SUBSCRIPTION_ID}
```

This will output something like:

```json
{
  "appId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "displayName": "NursingValidatorServicePrincipal",
  "password": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "tenant": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```

### Step 3: Update GitHub Secrets

Go to: https://github.com/ClinyQAi/open-nursing-core-ig/settings/secrets/actions

**Replace these 4 secrets** with the NEW values from step 2:

- `AZURE_CLIENT_ID` = the `appId` from step 2
- `AZURE_CLIENT_SECRET` = the `password` from step 2  
- `AZURE_TENANT_ID` = the `tenant` from step 2
- `AZURE_SUBSCRIPTION_ID` = your subscription ID from step 1

Keep the existing Azure OpenAI secrets unchanged.

### Step 4: Retry Deployment

1. Go to: https://github.com/ClinyQAi/open-nursing-core-ig/actions
2. Click **"Deploy to Azure"** workflow
3. Click **"Run workflow"**
4. Wait 7-10 minutes

---

## Why This Happened

The previous service principal was created in the "Microsoft Accounts" tenant instead of your organization's Azure tenant. Each tenant is a separate Azure AD directory, and applications must be registered in the same tenant as your subscription.

---

## Need Help?

If you're unsure about your tenant ID, run:

```bash
az account show --query tenantId
```

This will display your current tenant ID.

---

**Action Required**: Complete steps 1-3 above, then retry deployment in GitHub Actions.
