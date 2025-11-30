# Phase 3 Production Deployment Guide

## 🚀 Overview

The NHS Unified Nursing Validator Phase 3 is ready for production deployment across multiple cloud platforms. This guide provides step-by-step instructions for deployment on Azure, Heroku, or Kubernetes.

## 📋 Prerequisites

- Docker installed locally
- Cloud provider credentials (Azure CLI, Heroku CLI, or kubectl)
- GitHub repository access
- `.env.production` configured with production secrets

## 🏗️ Architecture

### Application Stack
- **Frontend**: Streamlit 1.51.0
- **Backend**: Python 3.11
- **ML Engine**: scikit-learn, SHAP, plotly
- **Vector DB**: Chroma
- **Auth**: Role-based access control (Admin, Clinician, Nurse)

### Phase 3 Features
- 🤖 **Predictive Analytics**: Readmission/deterioration risk prediction
- 💡 **Recommendations**: AI-powered care plan optimization
- 🚨 **Anomaly Detection**: Real-time vital sign monitoring
- 📊 **Dashboards**: Model performance and explainability

---

## 🔷 Azure Container Instances Deployment

### Option 1: Using Azure CLI

```bash
# 1. Create resource group
az group create \
  --name nursing-validator-prod \
  --location uksouth

# 2. Create container registry (optional)
az acr create \
  --resource-group nursing-validator-prod \
  --name nursingvalidatoracr \
  --sku Basic

# 3. Build image
az acr build \
  --registry nursingvalidatoracr \
  --image nursing-validator:latest \
  --file Dockerfile .

# 4. Deploy to Container Instances
az container create \
  --resource-group nursing-validator-prod \
  --name nursing-validator \
  --image nursingvalidatoracr.azurecr.io/nursing-validator:latest \
  --cpu 2 \
  --memory 4 \
  --ports 8501 \
  --environment-variables \
    APP_ENV=production \
    LOG_LEVEL=info \
  --secure-environment-variables \
    AZURE_OPENAI_ENDPOINT="https://your-resource.openai.azure.com/" \
    AZURE_OPENAI_API_KEY="your-api-key" \
    AZURE_OPENAI_API_VERSION="2024-01-15" \
    AZURE_OPENAI_DEPLOYMENT="gpt-4o" \
  --restart-policy OnFailure

# 5. Get container URL
az container show \
  --resource-group nursing-validator-prod \
  --name nursing-validator \
  --query ipAddress.fqdn
```

### Option 2: Using Azure App Service (Recommended)

```bash
# 1. Create App Service Plan
az appservice plan create \
  --name nursing-validator-plan \
  --resource-group nursing-validator-prod \
  --sku B2 \
  --is-linux

# 2. Create Web App with Docker
az webapp create \
  --resource-group nursing-validator-prod \
  --plan nursing-validator-plan \
  --name nursing-validator \
  --deployment-container-image-name-user "nursingvalidatoracr.azurecr.io/nursing-validator:latest"

# 3. Configure deployment
az webapp deployment container config \
  --name nursing-validator \
  --resource-group nursing-validator-prod \
  --enable-cd true

# 4. Set environment variables
az webapp config appsettings set \
  --name nursing-validator \
  --resource-group nursing-validator-prod \
  --settings \
    APP_ENV=production \
    AZURE_OPENAI_ENDPOINT="https://your-resource.openai.azure.com/" \
    AZURE_OPENAI_API_KEY="your-api-key" \
    WEBSITES_PORT=8501
```

---

## 🟣 Heroku Deployment

### Option 1: Using Heroku CLI

```bash
# 1. Login to Heroku
heroku login

# 2. Create app
heroku create nursing-validator

# 3. Add Buildpacks
heroku buildpacks:add --index 1 heroku/python

# 4. Set environment variables
heroku config:set \
  APP_ENV=production \
  AZURE_OPENAI_ENDPOINT="https://your-resource.openai.azure.com/" \
  AZURE_OPENAI_API_KEY="your-api-key"

# 5. Deploy
git push heroku main

# 6. View logs
heroku logs --tail
```

### Option 2: Using Docker with Heroku Container Registry

```bash
# 1. Login
heroku login
heroku container:login

# 2. Build and push
heroku container:push web --app nursing-validator

# 3. Release
heroku container:release web --app nursing-validator

# 4. Monitor
heroku open
heroku logs --tail
```

### Option 3: Connect GitHub Repository (Automated)

1. Visit [Heroku Dashboard](https://dashboard.heroku.com)
2. Create new app
3. Connect to GitHub repository
4. Enable automatic deploys from `main` branch
5. Set environment variables in Settings > Config Vars
6. Deploy

---

## ☸️ Kubernetes Deployment

### Prerequisites
- kubectl configured
- Access to Kubernetes cluster
- Docker image pushed to registry

### Step-by-Step Deployment

```bash
# 1. Create namespace
kubectl create namespace nursing-validator

# 2. Create ConfigMap for settings
kubectl create configmap nursing-config \
  --from-literal=APP_ENV=production \
  --from-literal=LOG_LEVEL=info \
  --namespace=nursing-validator

# 3. Create Secrets for sensitive data
kubectl create secret generic nursing-secrets \
  --from-literal=AZURE_OPENAI_ENDPOINT="https://your-resource.openai.azure.com/" \
  --from-literal=AZURE_OPENAI_API_KEY="your-api-key" \
  --from-literal=AZURE_OPENAI_API_VERSION="2024-01-15" \
  --from-literal=AZURE_OPENAI_DEPLOYMENT="gpt-4o" \
  --namespace=nursing-validator

# 4. Deploy using kubectl
kubectl apply -f k8s-deployment.yaml --namespace=nursing-validator

# 5. Verify deployment
kubectl get pods --namespace=nursing-validator
kubectl logs -f deployment/nursing-validator --namespace=nursing-validator

# 6. Access application
kubectl port-forward svc/nursing-validator 8501:8501 --namespace=nursing-validator
```

### Kubernetes Manifest (k8s-deployment.yaml)

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: nursing-data
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nursing-validator
  labels:
    app: nursing-validator
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nursing-validator
  template:
    metadata:
      labels:
        app: nursing-validator
    spec:
      containers:
      - name: nursing-validator
        image: your-registry/nursing-validator:latest
        ports:
        - containerPort: 8501
        resources:
          requests:
            cpu: 1000m
            memory: 2Gi
          limits:
            cpu: 2000m
            memory: 4Gi
        envFrom:
        - configMapRef:
            name: nursing-config
        - secretRef:
            name: nursing-secrets
        volumeMounts:
        - name: data
          mountPath: /app/data
        livenessProbe:
          httpGet:
            path: /
            port: 8501
          initialDelaySeconds: 40
          periodSeconds: 30
        readinessProbe:
          httpGet:
            path: /
            port: 8501
          initialDelaySeconds: 20
          periodSeconds: 10
      volumes:
      - name: data
        persistentVolumeClaim:
          claimName: nursing-data

---
apiVersion: v1
kind: Service
metadata:
  name: nursing-validator
spec:
  selector:
    app: nursing-validator
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8501
  type: LoadBalancer
```

---

## 🔒 Security Best Practices

### Environment Variables
Always use `.env.production` for sensitive data:

```env
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=your-secure-api-key
DB_PASSWORD=secure-password-here
SESSION_TIMEOUT_MINUTES=30
ENABLE_AUTHENTICATION=true
```

### Docker Security
- Non-root user (nursing:nursing)
- Read-only root filesystem where possible
- Security options: `no-new-privileges`
- Regular image scanning

### Network Security
- Enable XSRF protection (already enabled)
- Disable CORS for untrusted origins
- Use HTTPS/TLS in production
- Implement rate limiting

---

## 🧪 Testing Deployment

### Health Check
```bash
curl -f http://your-deployment-url:8501/
```

### Login Test
```bash
# Use default credentials (change in production)
Username: admin
Password: admin2025
```

### ML Features Test
1. Navigate to "🤖 ML Predictions" tab
2. Check predictive models load
3. Navigate to "💡 Recommendations" tab
4. Verify recommendations display
5. Navigate to "🚨 Anomalies" tab
6. Check anomaly alerts show

---

## 📊 Monitoring & Logging

### Azure App Insights
```bash
az monitor app-insights component create \
  --app nursing-validator \
  --location uksouth \
  --resource-group nursing-validator-prod
```

### Heroku Metrics
```bash
heroku metrics:dyno --app nursing-validator
```

### Kubernetes Monitoring
```bash
# CPU/Memory usage
kubectl top pods --namespace=nursing-validator

# Pod logs
kubectl logs -f pod/nursing-validator-xxx --namespace=nursing-validator
```

---

## 🔄 CI/CD Pipeline

The repository includes GitHub Actions workflow (`production-deploy.yml`) that:

1. **Test** - Syntax and code quality checks
2. **Build** - Docker image creation and push
3. **Deploy Staging** - Deploy to staging environment
4. **Integration Tests** - Run test suite
5. **Deploy Production** - Manual approval required

### Triggering Deployment
```bash
# Automatic on main branch push
git push origin main

# Manual trigger
gh workflow run production-deploy.yml -f environment=production
```

---

## 🆘 Troubleshooting

### Container fails to start
```bash
# Check logs
docker logs nursing-validator

# Verify environment variables
echo $AZURE_OPENAI_ENDPOINT
echo $AZURE_OPENAI_API_KEY
```

### Health check failing
```bash
# Check port 8501 is accessible
curl -v http://localhost:8501/

# Check Streamlit logs
tail -f /app/logs/app.log
```

### Authentication issues
- Verify `.env.production` credentials
- Check database connectivity
- Ensure timezone alignment

---

## 📚 Additional Resources

- [Streamlit Deployment](https://docs.streamlit.io/streamlit-cloud/deploy-your-app)
- [Azure Container Instances](https://docs.microsoft.com/azure/container-instances/)
- [Heroku Python Support](https://devcenter.heroku.com/articles/python-support)
- [Kubernetes Documentation](https://kubernetes.io/docs/)

---

## ✅ Deployment Checklist

- [ ] `.env.production` configured with real credentials
- [ ] Docker image tested locally
- [ ] Health checks passing
- [ ] All Phase 3 ML modules loading
- [ ] Authentication working
- [ ] Database connectivity verified
- [ ] Azure/Heroku/K8s credentials configured
- [ ] GitHub Actions secrets configured
- [ ] Monitoring and logging setup
- [ ] Backup strategy in place

---

**Last Updated**: November 30, 2025  
**Phase**: 3 (ML & Dashboards)  
**Status**: Ready for Deployment
