# 🚀 Production Deployment Quick Start

## 30-Minute Setup for Azure

### Prerequisites
- Azure subscription (free tier available)
- Azure CLI installed: https://docs.microsoft.com/cli/azure/install-azure-cli
- Docker installed (if deploying locally first)
- GitHub account with this repository forked

### Step 1: Set Up Azure Resources (5 minutes)

```bash
# Login to Azure
az login

# Create resource group
az group create \
  --name nursing-validator \
  --location eastus

# Create container registry
az acr create \
  --resource-group nursing-validator \
  --name nursingvalidator \
  --sku Basic

# Get registry credentials
az acr credential show \
  --resource-group nursing-validator \
  --name nursingvalidator
```

### Step 2: Configure Secrets (5 minutes)

**Option A: Using Azure Key Vault (Recommended)**
```bash
# Create Key Vault
az keyvault create \
  --resource-group nursing-validator \
  --name nursing-validator-kv

# Store secrets
az keyvault secret set \
  --vault-name nursing-validator-kv \
  --name azure-openai-endpoint \
  --value "https://your-resource.openai.azure.com/"

az keyvault secret set \
  --vault-name nursing-validator-kv \
  --name azure-openai-api-key \
  --value "your_api_key_here"

az keyvault secret set \
  --vault-name nursing-validator-kv \
  --name azure-openai-deployment \
  --value "gpt-4o"
```

**Option B: Using GitHub Secrets**
1. Go to repository Settings → Secrets and variables → Actions
2. Create secrets:
   - `AZURE_OPENAI_ENDPOINT`
   - `AZURE_OPENAI_API_KEY`
   - `AZURE_OPENAI_DEPLOYMENT`

### Step 3: Build and Push Docker Image (10 minutes)

```bash
# Clone repository
git clone https://github.com/YOUR-USERNAME/open-nursing-core-ig.git
cd open-nursing-core-ig

# Build Docker image
docker build -t nursingvalidator.azurecr.io/nursing-validator:latest .

# Push to Azure Container Registry
az acr login --name nursingvalidator
docker push nursingvalidator.azurecr.io/nursing-validator:latest
```

### Step 4: Deploy Container (10 minutes)

```bash
# Deploy to Azure Container Instances
az container create \
  --resource-group nursing-validator \
  --name nursing-validator \
  --image nursingvalidator.azurecr.io/nursing-validator:latest \
  --cpu 2 \
  --memory 4 \
  --registry-login-server nursingvalidator.azurecr.io \
  --registry-username <username-from-step-2> \
  --registry-password <password-from-step-2> \
  --ports 8501 \
  --dns-name-label nursing-validator \
  --environment-variables \
    APP_ENV=production \
    LOG_LEVEL=info \
    AZURE_OPENAI_ENDPOINT="https://your-resource.openai.azure.com/" \
    AZURE_OPENAI_DEPLOYMENT=gpt-4o \
  --secure-environment-variables \
    AZURE_OPENAI_API_KEY=your_api_key_here
```

### Step 5: Verify Deployment

```bash
# Check container status
az container show \
  --resource-group nursing-validator \
  --name nursing-validator

# View logs
az container logs \
  --resource-group nursing-validator \
  --name nursing-validator

# Get public URL
az container show \
  --resource-group nursing-validator \
  --name nursing-validator \
  --query ipAddress.fqdn --output tsv
```

**Access your app at:**
```
http://nursing-validator.eastus.azurecontainer.io:8501
```

---

## 🐳 Docker Compose (Local Production Testing)

### Quick Start with docker-compose

```bash
# 1. Create production environment file
cat > .env.production << 'EOF'
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=your_api_key
AZURE_OPENAI_API_VERSION=2024-01-15
AZURE_OPENAI_DEPLOYMENT=gpt-4o
LOG_LEVEL=info
EOF

# 2. Start services
docker-compose --env-file .env.production up -d

# 3. Check status
docker-compose ps

# 4. View logs
docker-compose logs -f nursing-validator

# 5. Access application
# Open http://localhost:8501

# 6. Stop services
docker-compose down
```

---

## ☁️ Alternative: Heroku Deployment (Free Tier)

### Prerequisites
- Heroku account (https://www.heroku.com)
- Heroku CLI installed

### Deploy

```bash
# Login to Heroku
heroku login

# Create app
heroku create nursing-validator

# Add buildpack for Python
heroku buildpacks:add heroku/python

# Set environment variables
heroku config:set AZURE_OPENAI_ENDPOINT="https://your-resource.openai.azure.com/"
heroku config:set AZURE_OPENAI_API_KEY="your_api_key"
heroku config:set AZURE_OPENAI_DEPLOYMENT="gpt-4o"
heroku config:set APP_ENV="production"

# Create Procfile (if not exists)
echo "web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0" > Procfile

# Deploy
git push heroku main

# View logs
heroku logs --tail
```

**Access at:** `https://nursing-validator.herokuapp.com`

---

## 🔒 Security Best Practices

### Before Going Live

- [ ] Change all default credentials
- [ ] Enable HTTPS/SSL
- [ ] Configure firewall rules
- [ ] Set up monitoring and alerting
- [ ] Enable backup and recovery
- [ ] Review audit logs
- [ ] Implement rate limiting
- [ ] Add authentication middleware

### Environment Variables

**NEVER commit these to GitHub:**
```bash
AZURE_OPENAI_API_KEY=xxx
AZURE_OPENAI_ENDPOINT=xxx
```

Use GitHub Secrets or Azure Key Vault instead.

---

## 📊 Monitoring Your Deployment

### View Logs

```bash
# Azure Container Instances
az container logs \
  --resource-group nursing-validator \
  --name nursing-validator

# Docker
docker logs nursing-validator

# Docker Compose
docker-compose logs nursing-validator
```

### Set Up Alerts

**In Azure Portal:**
1. Search for "Container Instances"
2. Select your container
3. Go to "Alerts" → "New alert rule"
4. Set conditions (CPU > 80%, Memory > 90%, etc.)
5. Configure action group (email, webhook, etc.)

### Health Check

```bash
# Test endpoint
curl -f http://nursing-validator.eastus.azurecontainer.io:8501/

# Continuous monitoring
watch 'curl -s http://nursing-validator.eastus.azurecontainer.io:8501/ && echo "OK"'
```

---

## 🔄 Backup & Restore

### Create Backup

```bash
# For Docker
docker exec nursing-validator \
  tar -czf /tmp/backup.tar.gz chroma_db_fons/ .chat_history.json

docker cp nursing-validator:/tmp/backup.tar.gz ./backup.tar.gz

# For Azure
az container exec \
  --resource-group nursing-validator \
  --name nursing-validator \
  --exec-command "tar -czf /tmp/backup.tar.gz chroma_db_fons/"
```

### Restore Backup

```bash
# Extract backup
tar -xzf backup.tar.gz

# Restart container
docker restart nursing-validator
```

---

## 🆘 Troubleshooting

### Container won't start

```bash
# Check logs
docker logs nursing-validator

# Check image exists
docker images

# Try with more memory
docker run -m 4g nursing-validator:latest
```

### Knowledge base offline

```bash
# Rebuild database
docker exec nursing-validator python ingest_fast.py

# Check permissions
docker exec nursing-validator ls -la chroma_db_fons/
```

### Chat history not saving

```bash
# Check file permissions
docker exec nursing-validator chmod 666 .chat_history.json

# Verify write access
docker exec nursing-validator touch .chat_history.json
```

### Performance issues

```bash
# Check resource usage
docker stats nursing-validator

# Increase limits
docker update --memory 8g --cpus 2 nursing-validator
```

---

## 📞 Support & Next Steps

✅ **Deployment Complete!** Your app is now running in production.

### What's Next?

1. **Custom Domain**: Set up custom domain with SSL
2. **CI/CD Pipeline**: Automate deployments with GitHub Actions
3. **Database**: Migrate to PostgreSQL for better scalability
4. **Monitoring**: Set up comprehensive monitoring and logging
5. **Backup**: Configure automated daily backups

### Resources

- Full deployment guide: See `PRODUCTION_DEPLOYMENT.md`
- Features documentation: See `FEATURES.md`
- Quick reference: See `QUICK_REFERENCE.md`
- GitHub Issues: Report problems or request features

---

**Your app is live! 🎉**

Share your deployment URL with the team and start collecting feedback.

---

**Last Updated:** November 29, 2025
