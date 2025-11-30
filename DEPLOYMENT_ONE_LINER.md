# Azure Deployment - One-Liner Quick Start

## 🚀 Ready to Deploy!

Your application is configured and ready for Azure deployment.

### Prerequisites
- ✅ Azure CLI installed on your local machine
- ✅ Azure account with an active subscription
- ✅ Credentials configured in `.env.production`

### One-Liner Deployment Command

**Run this on your local machine (Terminal or PowerShell):**

```bash
az login && cd /path/to/open-nursing-core-ig && bash deploy-azure.sh
```

Replace `/path/to/open-nursing-core-ig` with your actual project directory path.

### Example (for different systems):

**Linux/macOS:**
```bash
az login && cd ~/Projects/open-nursing-core-ig && bash deploy-azure.sh
```

**Windows PowerShell:**
```powershell
az login; cd C:\Projects\open-nursing-core-ig; bash deploy-azure.sh
```

---

## What Happens Next

The script will automatically:

1. **Build Docker Image**
   - Compiles your Python application into a container image
   - Optimized for production with multi-stage build

2. **Create Azure Resources**
   - Resource Group: `nursing-validator-prod`
   - Container Registry: `nursingvalidatoracr`
   - Sets up in UK South region (uksouth)

3. **Push Image to Registry**
   - Uploads your Docker image to Azure Container Registry
   - ~100-200 MB compressed size

4. **Deploy to Azure Container Instances**
   - Creates container: `nursing-validator`
   - Allocates 2 CPU cores and 4 GB memory
   - Assigns public IP address
   - Configures environment variables

5. **Display Your Public URL**
   - Example: `http://nursing-validator.uksouth.azurecontainers.io:8501`
   - Ready to access immediately

---

## ⏱️ Timeline

| Step | Duration |
|------|----------|
| Azure Login | 30 seconds |
| Docker Build | 2-3 minutes |
| Registry Creation | 1-2 minutes |
| Image Push | 1-2 minutes |
| Container Deploy | 1-2 minutes |
| Total | **5-10 minutes** |

---

## 🔑 Configuration Deployed

The following credentials are securely passed to the container:

```
AZURE_OPENAI_ENDPOINT: https://nursing-brain-uk-685.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT: gpt-4o
AZURE_OPENAI_API_VERSION: 2024-08-01-preview
AZURE_OPENAI_API_KEY: [SECRET - from .env.production]
```

---

## ✅ After Deployment

Once complete, you'll see:

```
✅ Deployment Complete!

Access your application at:
http://nursing-validator.uksouth.azurecontainers.io:8501
```

1. **Open the URL** in your browser
2. **Login** with credentials:
   - Username: `admin`
   - Password: `admin2025`
3. **Test the application**
   - Try the Chat tab
   - View Predictions dashboard
   - Test Recommendations
   - Check Anomaly Detection

---

## 📊 Monitoring Your Deployment

After deployment, use these commands to monitor your container:

**Check logs:**
```bash
az container logs --resource-group nursing-validator-prod \
                  --name nursing-validator
```

**View status:**
```bash
az container show --resource-group nursing-validator-prod \
                  --name nursing-validator
```

**Get IP address:**
```bash
az container show --resource-group nursing-validator-prod \
                  --name nursing-validator \
                  --query ipAddress.fqdn
```

---

## 🛑 Stopping & Cleanup

**Stop the container:**
```bash
az container stop --resource-group nursing-validator-prod \
                  --name nursing-validator
```

**Delete everything:**
```bash
az group delete --resource-group nursing-validator-prod
```

---

## ❓ Troubleshooting

**"az login: command not found"**
- Install Azure CLI: https://learn.microsoft.com/en-us/cli/azure/install-azure-cli

**"Failed to authenticate"**
- Ensure your Azure account has an active subscription
- Try: `az account list` to see your subscriptions

**"Permission denied"**
- Ensure you have permissions to create resources
- Contact your Azure subscription administrator

**Docker build fails**
- Check Docker is installed and running on your machine
- Ensure you have internet connection
- Try running: `docker --version`

---

## 📝 Notes

- The deployment creates resources in **UK South region** (uksouth)
- Container runs with restart policy: **OnFailure**
- Public IP is automatically assigned
- No additional configuration needed after deployment
- Application starts on port **8501** (Streamlit default)

---

**Need help?** Check the detailed guides:
- `DEPLOYMENT_GUIDE.md` - Full step-by-step instructions
- `QUICK_DEPLOYMENT.md` - Platform comparison and timing
- `deploy-azure.sh` - The actual deployment script

