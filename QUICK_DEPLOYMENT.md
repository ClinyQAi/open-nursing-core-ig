# 🚀 NHS Nursing Validator Phase 3 - Quick Deployment Guide

## Choose Your Deployment Platform

### ☁️ **Azure (Recommended for NHS)**
Best for: Enterprise, healthcare compliance, FIPS-140 support

```bash
# 1. Install Azure CLI
# https://docs.microsoft.com/en-us/cli/azure/install-azure-cli

# 2. Configure .env.production with your credentials
nano .env.production

# 3. Run deployment script
bash deploy-azure.sh

# 4. Access your app
# URL will be provided after successful deployment
```

**Time to Deploy**: ~10-15 minutes  
**Cost**: $0.0106/second (≈$50-100/month for 2 CPU, 4GB RAM)

---

### 🟣 **Heroku (Easiest for Small Teams)**
Best for: Quick setup, GitHub integration, auto-scaling

```bash
# 1. Install Heroku CLI
# https://devcenter.heroku.com/articles/heroku-cli

# 2. Configure .env.production
nano .env.production

# 3. Run deployment script
bash deploy-heroku.sh

# 4. Access your app
# https://nursing-validator.herokuapp.com/
```

**Time to Deploy**: ~5-10 minutes  
**Cost**: $25-50/month (free tier available with limitations)

---

### ☸️ **Kubernetes (Best for Large Deployments)**
Best for: High availability, auto-scaling, multi-region

```bash
# 1. Install kubectl
# https://kubernetes.io/docs/tasks/tools/

# 2. Configure kubeconfig
# Set up connection to your Kubernetes cluster

# 3. Configure .env.production
nano .env.production

# 4. Update image name in deploy-kubernetes.sh
sed -i 's|your-registry|your-actual-registry|g' deploy-kubernetes.sh

# 5. Run deployment script
bash deploy-kubernetes.sh

# 6. Access via port-forward
kubectl port-forward svc/nursing-validator 8501:80 -n nursing-validator
```

**Time to Deploy**: ~15-20 minutes  
**Cost**: Varies by provider ($20-100+/month)

---

## 📋 Pre-Deployment Checklist

Before deploying, ensure:

- [ ] Docker installed locally (for testing)
- [ ] `.env.production` configured with:
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_API_VERSION`
  - `AZURE_OPENAI_DEPLOYMENT`
- [ ] Cloud platform CLI installed (az/heroku/kubectl)
- [ ] Cloud credentials configured
- [ ] GitHub repository up to date
- [ ] All Phase 3 ML modules tested locally

---

## 🧪 Local Testing Before Deployment

```bash
# 1. Test Docker build
docker build -t nursing-validator:test .

# 2. Run container locally
docker run -p 8501:8501 \
  -e AZURE_OPENAI_ENDPOINT="your-endpoint" \
  -e AZURE_OPENAI_API_KEY="your-key" \
  nursing-validator:test

# 3. Access at http://localhost:8501
# Login with: admin / admin2025

# 4. Test Phase 3 features
# - Click "🤖 ML Predictions" tab
# - Click "💡 Recommendations" tab
# - Click "🚨 Anomalies" tab
```

---

## 🔐 Security Configuration

### API Keys & Credentials
Never commit `.env.production` to git!

```bash
# Add to .gitignore
echo ".env.production" >> .gitignore
echo ".env.production.save" >> .gitignore

# Use secret management:
# - Azure Key Vault (Azure)
# - Heroku Config Vars (Heroku)
# - Kubernetes Secrets (K8s)
```

### HTTPS/TLS
All deployments support HTTPS in production.

**Azure**: Auto-configured with Azure App Service  
**Heroku**: Free Let's Encrypt certificate included  
**K8s**: Configure via cert-manager or ingress controller

---

## 🚨 Troubleshooting

### Container won't start
```bash
# Check logs
docker logs nursing-validator

# Verify environment variables
docker inspect nursing-validator

# Test locally first
docker run -it nursing-validator:test bash
```

### Health check failing
```bash
# Check port accessibility
curl -v http://localhost:8501/

# Verify Streamlit is running
ps aux | grep streamlit

# Check logs
tail -f /app/logs/app.log
```

### Authentication not working
- Verify `.env.production` is loaded
- Check database connectivity
- Ensure credentials match in all layers

---

## 📊 Post-Deployment Validation

After deployment:

1. **Access Application**
   ```bash
   curl -f https://your-deployment-url/
   ```

2. **Login Test**
   - Username: `admin`
   - Password: `admin2025`

3. **ML Features Test**
   - Check "🤖 ML Predictions" loads
   - Verify "💡 Recommendations" show
   - Confirm "🚨 Anomalies" tab works

4. **Monitor Logs**
   ```bash
   # Azure
   az container logs --name nursing-validator

   # Heroku
   heroku logs --tail

   # Kubernetes
   kubectl logs -f deployment/nursing-validator
   ```

---

## 🔄 CI/CD Integration

Automatic deployment on push to main:

```bash
# GitHub Actions will:
# 1. Test code
# 2. Build Docker image
# 3. Deploy to staging
# 4. Run integration tests
# 5. Deploy to production (with approval)
```

Monitor in: **GitHub > Actions tab**

---

## 💾 Backup & Recovery

### Azure
```bash
az container export -g nursing-validator-prod -n nursing-validator
```

### Heroku
```bash
heroku pg:backups:capture
heroku pg:backups:download
```

### Kubernetes
```bash
kubectl get pvc -n nursing-validator
# Backup persistent volume
```

---

## 📞 Support & Resources

- **Deployment Issues**: Check logs in cloud console
- **ML Features**: See `PHASE3_ML.md`
- **Azure Help**: https://docs.microsoft.com/azure/
- **Heroku Help**: https://devcenter.heroku.com/
- **K8s Help**: https://kubernetes.io/docs/

---

**Status**: ✅ Ready to Deploy  
**Last Updated**: November 30, 2025  
**Version**: Phase 3 - ML & Dashboards
