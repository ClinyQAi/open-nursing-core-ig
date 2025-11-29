# Production Deployment Guide

## 🚀 Overview

This guide covers deploying the NHS Nursing Validator to production across multiple platforms.

## Pre-Deployment Checklist

### ✅ Security
- [ ] Change all default credentials
- [ ] Set up environment variables in `.env`
- [ ] Enable HTTPS/SSL certificates
- [ ] Configure firewall rules
- [ ] Review DEPLOYMENT.md security section
- [ ] Enable audit logging

### ✅ Configuration
- [ ] Create `.env.production` with real credentials
- [ ] Set `APP_ENV=production`
- [ ] Configure logging level
- [ ] Set up database (for Phase 2)
- [ ] Configure storage backend

### ✅ Data
- [ ] Backup current knowledge base
- [ ] Verify chat history file
- [ ] Test backup/restore procedures

### ✅ Testing
- [ ] Test locally with `streamlit run app.py`
- [ ] Verify all features work
- [ ] Test with demo credentials
- [ ] Check chat history saving
- [ ] Verify visualizations load

---

## 🐳 Docker Deployment (Recommended)

### Build the Docker Image

```bash
# Clone the repository
git clone https://github.com/ClinyQAi/open-nursing-core-ig.git
cd open-nursing-core-ig

# Build the image
docker build -t nursing-validator:latest .

# Tag for registry (example: Docker Hub)
docker tag nursing-validator:latest yourusername/nursing-validator:latest

# Push to registry
docker push yourusername/nursing-validator:latest
```

### Run Locally with Docker

```bash
# Create .env.production file with your credentials
cat > .env.production << 'EOF'
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=your_api_key
AZURE_OPENAI_API_VERSION=2024-01-15
AZURE_OPENAI_DEPLOYMENT=gpt-4o
APP_ENV=production
LOG_LEVEL=info
EOF

# Run the container
docker run -p 8501:8501 \
  --env-file .env.production \
  -v $(pwd)/chroma_db_fons:/app/chroma_db_fons \
  -v $(pwd)/.chat_history.json:/app/.chat_history.json \
  nursing-validator:latest
```

Access at: http://localhost:8501

---

## ☁️ Azure Container Instances

### Prerequisites
- Azure subscription
- Azure CLI installed
- Azure Container Registry

### Deploy

```bash
# Login to Azure
az login

# Create resource group
az group create --name nursing-validator --location eastus

# Create container registry
az acr create --resource-group nursing-validator \
  --name nursingvalidator \
  --sku Basic

# Push image to ACR
az acr build --registry nursingvalidator \
  --image nursing-validator:latest .

# Deploy container
az container create \
  --resource-group nursing-validator \
  --name nursing-validator \
  --image nursingvalidator.azurecr.io/nursing-validator:latest \
  --cpu 2 --memory 4 \
  --registry-login-server nursingvalidator.azurecr.io \
  --registry-username <username> \
  --registry-password <password> \
  --ports 8501 \
  --dns-name-label nursing-validator \
  --environment-variables \
    APP_ENV=production \
    AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/ \
  --secure-environment-variables \
    AZURE_OPENAI_API_KEY=your_api_key \
    AZURE_OPENAI_DEPLOYMENT=gpt-4o
```

Access at: http://nursing-validator.eastus.azurecontainer.io:8501

### View Logs
```bash
az container logs --resource-group nursing-validator \
  --name nursing-validator
```

---

## ☁️ Azure App Service

### Prerequisites
- Azure subscription
- Azure CLI
- Docker image in ACR

### Deploy

```bash
# Create App Service Plan
az appservice plan create \
  --name nursing-validator-plan \
  --resource-group nursing-validator \
  --sku B2 --is-linux

# Create Web App
az webapp create \
  --resource-group nursing-validator \
  --plan nursing-validator-plan \
  --name nursing-validator \
  --deployment-container-image-name nursingvalidator.azurecr.io/nursing-validator:latest

# Configure container
az webapp config container set \
  --name nursing-validator \
  --resource-group nursing-validator \
  --docker-custom-image-name nursingvalidator.azurecr.io/nursing-validator:latest \
  --docker-registry-server-url https://nursingvalidator.azurecr.io \
  --docker-registry-server-user <username> \
  --docker-registry-server-password <password>

# Set environment variables
az webapp config appsettings set \
  --resource-group nursing-validator \
  --name nursing-validator \
  --settings \
    APP_ENV=production \
    AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
    WEBSITES_PORT=8501

# Set secure environment variables
az webapp config appsettings set \
  --resource-group nursing-validator \
  --name nursing-validator \
  --settings \
    AZURE_OPENAI_API_KEY=your_api_key \
    AZURE_OPENAI_DEPLOYMENT=gpt-4o
```

Access at: https://nursing-validator.azurewebsites.net

---

## ☁️ Kubernetes (Production at Scale)

### Prerequisites
- Azure Kubernetes Service (AKS) cluster
- kubectl configured

### Create Deployment YAML

```bash
cat > k8s-deployment.yaml << 'EOF'
apiVersion: v1
kind: Namespace
metadata:
  name: nursing-validator

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nursing-validator
  namespace: nursing-validator
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
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
        image: nursingvalidator.azurecr.io/nursing-validator:latest
        ports:
        - containerPort: 8501
        env:
        - name: APP_ENV
          value: "production"
        - name: AZURE_OPENAI_ENDPOINT
          valueFrom:
            secretKeyRef:
              name: azure-credentials
              key: endpoint
        - name: AZURE_OPENAI_API_KEY
          valueFrom:
            secretKeyRef:
              name: azure-credentials
              key: api-key
        resources:
          requests:
            memory: "2Gi"
            cpu: "500m"
          limits:
            memory: "4Gi"
            cpu: "1000m"
        livenessProbe:
          httpGet:
            path: /
            port: 8501
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /
            port: 8501
          initialDelaySeconds: 10
          periodSeconds: 5

---
apiVersion: v1
kind: Service
metadata:
  name: nursing-validator-service
  namespace: nursing-validator
spec:
  type: LoadBalancer
  selector:
    app: nursing-validator
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8501

---
apiVersion: v1
kind: Secret
metadata:
  name: azure-credentials
  namespace: nursing-validator
type: Opaque
stringData:
  endpoint: "https://your-resource.openai.azure.com/"
  api-key: "your_api_key"
EOF
```

### Deploy

```bash
# Create secrets
kubectl create secret generic azure-credentials \
  --from-literal=endpoint=https://your-resource.openai.azure.com/ \
  --from-literal=api-key=your_api_key \
  -n nursing-validator

# Apply deployment
kubectl apply -f k8s-deployment.yaml

# Check status
kubectl get deployments -n nursing-validator
kubectl get pods -n nursing-validator
kubectl get services -n nursing-validator

# Port forward for testing
kubectl port-forward svc/nursing-validator-service 8501:80 -n nursing-validator
```

Access at: http://localhost:8501

---

## 🔒 HTTPS/SSL Configuration

### Using Let's Encrypt with nginx

```bash
# Create nginx config
cat > nginx.conf << 'EOF'
upstream streamlit {
    server localhost:8501;
}

server {
    listen 443 ssl http2;
    server_name your-domain.com;

    ssl_certificate /etc/letsencrypt/live/your-domain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/your-domain.com/privkey.pem;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;

    location / {
        proxy_pass http://streamlit;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}

server {
    listen 80;
    server_name your-domain.com;
    return 301 https://$server_name$request_uri;
}
EOF
```

---

## 📊 Monitoring & Logging

### Application Logs

```bash
# View logs in Docker
docker logs -f container_id

# View logs in Kubernetes
kubectl logs -f deployment/nursing-validator -n nursing-validator

# View logs in Azure
az container logs --resource-group nursing-validator \
  --name nursing-validator
```

### Log Files

The application logs to:
- `stdout` (console)
- `/app/logs/app.log` (file, in production)

### Integration Options

```python
# Sentry (Error Tracking)
SENTRY_DSN=https://your-sentry-dsn

# Datadog (Monitoring)
DATADOG_API_KEY=your_datadog_key

# Application Insights (Azure)
APPINSIGHTS_INSTRUMENTATION_KEY=your_key
```

---

## 🔄 Backup & Recovery

### Backup Strategy

```bash
# Backup knowledge database
tar -czf backups/chroma_db_$(date +%Y%m%d_%H%M%S).tar.gz \
  chroma_db_fons/

# Backup chat history
cp .chat_history.json backups/.chat_history_$(date +%Y%m%d_%H%M%S).json

# Backup daily (cron job)
0 2 * * * /path/to/backup-script.sh
```

### Restore Procedure

```bash
# Restore knowledge database
tar -xzf backups/chroma_db_20251201_020000.tar.gz

# Restore chat history
cp backups/.chat_history_20251201_020000.json .chat_history.json

# Restart application
docker restart container_id
```

---

## 🚨 Health Checks

### Manual Health Check

```bash
curl -f http://localhost:8501/health || echo "Unhealthy"
```

### Automated Monitoring

```bash
# With curl in a loop
while true; do
  curl -f http://localhost:8501/ > /dev/null 2>&1
  if [ $? -ne 0 ]; then
    echo "Service down at $(date)" >> /var/log/health.log
    # Trigger alert or restart
  fi
  sleep 60
done
```

---

## 🔐 Production Security Checklist

- [ ] Enable HTTPS/SSL
- [ ] Set strong credentials
- [ ] Configure firewall
- [ ] Enable audit logging
- [ ] Set up monitoring
- [ ] Implement backups
- [ ] Enable CORS restrictions
- [ ] Set session timeout
- [ ] Configure rate limiting
- [ ] Implement Web Application Firewall (WAF)
- [ ] Regular security updates
- [ ] Penetration testing

---

## 🆘 Troubleshooting

### Port Already in Use
```bash
# Kill process on port 8501
lsof -ti:8501 | xargs kill -9
```

### Out of Memory
```bash
# Increase memory limits in Docker/K8s
# Docker: --memory 4g
# K8s: memory: "4Gi"
```

### Knowledge Base Not Loading
```bash
# Rebuild knowledge database
python ingest_fast.py

# Check permissions
ls -la chroma_db_fons/
```

### Chat History Not Saving
```bash
# Check file permissions
chmod 666 .chat_history.json

# Verify directory writable
ls -la | grep chat
```

---

## 📞 Support

- Review FEATURES.md for feature documentation
- Check DEPLOYMENT.md for detailed deployment info
- Open issues on GitHub for problems
- Review application logs for errors

---

**Last Updated:** November 29, 2025
