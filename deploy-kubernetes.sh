#!/bin/bash
# Kubernetes Deployment Script for NHS Nursing Validator Phase 3

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}=== NHS Nursing Validator Phase 3 - Kubernetes Deployment ===${NC}"
echo ""

# Configuration
NAMESPACE="nursing-validator"
DEPLOYMENT_NAME="nursing-validator"
IMAGE="your-registry/nursing-validator:latest"
REPLICAS=2

# Check prerequisites
echo "Checking prerequisites..."
command -v kubectl >/dev/null 2>&1 || { echo -e "${RED}❌ kubectl not installed${NC}"; exit 1; }
echo -e "${GREEN}✓ kubectl installed${NC}"

# Check cluster connectivity
echo "Checking Kubernetes cluster connectivity..."
kubectl cluster-info > /dev/null 2>&1 || { echo -e "${RED}❌ Cannot connect to cluster${NC}"; exit 1; }
echo -e "${GREEN}✓ Connected to cluster${NC}"

# Create namespace
echo ""
echo "Creating namespace: $NAMESPACE"
kubectl create namespace $NAMESPACE --dry-run=client -o yaml | kubectl apply -f -
echo -e "${GREEN}✓ Namespace created/exists${NC}"

# Create ConfigMap
echo ""
echo "Creating ConfigMap..."
kubectl create configmap nursing-config \
  --from-literal=APP_ENV=production \
  --from-literal=LOG_LEVEL=info \
  --namespace=$NAMESPACE \
  --dry-run=client -o yaml | kubectl apply -f -
echo -e "${GREEN}✓ ConfigMap created${NC}"

# Create Secrets
echo ""
echo "Creating Secrets..."

if [ ! -f ".env.production" ]; then
  echo -e "${RED}❌ .env.production not found${NC}"
  exit 1
fi

# Extract secrets
AZURE_OPENAI_ENDPOINT=$(grep AZURE_OPENAI_ENDPOINT .env.production | cut -d '=' -f 2-)
AZURE_OPENAI_API_KEY=$(grep AZURE_OPENAI_API_KEY .env.production | cut -d '=' -f 2-)
AZURE_OPENAI_API_VERSION=$(grep AZURE_OPENAI_API_VERSION .env.production | cut -d '=' -f 2-)
AZURE_OPENAI_DEPLOYMENT=$(grep AZURE_OPENAI_DEPLOYMENT .env.production | cut -d '=' -f 2-)

kubectl create secret generic nursing-secrets \
  --from-literal=AZURE_OPENAI_ENDPOINT="$AZURE_OPENAI_ENDPOINT" \
  --from-literal=AZURE_OPENAI_API_KEY="$AZURE_OPENAI_API_KEY" \
  --from-literal=AZURE_OPENAI_API_VERSION="$AZURE_OPENAI_API_VERSION" \
  --from-literal=AZURE_OPENAI_DEPLOYMENT="$AZURE_OPENAI_DEPLOYMENT" \
  --namespace=$NAMESPACE \
  --dry-run=client -o yaml | kubectl apply -f -
echo -e "${GREEN}✓ Secrets created${NC}"

# Create PersistentVolumeClaim
echo ""
echo "Creating PersistentVolumeClaim..."
kubectl apply -f - << EOF --namespace=$NAMESPACE
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
EOF
echo -e "${GREEN}✓ PersistentVolumeClaim created${NC}"

# Create Deployment
echo ""
echo "Creating Deployment..."
kubectl apply -f - << EOF --namespace=$NAMESPACE
apiVersion: apps/v1
kind: Deployment
metadata:
  name: $DEPLOYMENT_NAME
  labels:
    app: $DEPLOYMENT_NAME
spec:
  replicas: $REPLICAS
  selector:
    matchLabels:
      app: $DEPLOYMENT_NAME
  template:
    metadata:
      labels:
        app: $DEPLOYMENT_NAME
    spec:
      containers:
      - name: $DEPLOYMENT_NAME
        image: $IMAGE
        imagePullPolicy: Always
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
          timeoutSeconds: 5
          failureThreshold: 3
        readinessProbe:
          httpGet:
            path: /
            port: 8501
          initialDelaySeconds: 20
          periodSeconds: 10
          timeoutSeconds: 5
          failureThreshold: 2
      volumes:
      - name: data
        persistentVolumeClaim:
          claimName: nursing-data
EOF
echo -e "${GREEN}✓ Deployment created${NC}"

# Create Service
echo ""
echo "Creating Service..."
kubectl apply -f - << EOF --namespace=$NAMESPACE
apiVersion: v1
kind: Service
metadata:
  name: $DEPLOYMENT_NAME
  labels:
    app: $DEPLOYMENT_NAME
spec:
  selector:
    app: $DEPLOYMENT_NAME
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8501
  type: LoadBalancer
EOF
echo -e "${GREEN}✓ Service created${NC}"

# Create HorizontalPodAutoscaler
echo ""
echo "Creating HorizontalPodAutoscaler..."
kubectl apply -f - << EOF --namespace=$NAMESPACE
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: $DEPLOYMENT_NAME
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: $DEPLOYMENT_NAME
  minReplicas: 2
  maxReplicas: 5
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
EOF
echo -e "${GREEN}✓ HorizontalPodAutoscaler created${NC}"

# Wait for deployment
echo ""
echo "Waiting for deployment to be ready..."
kubectl rollout status deployment/$DEPLOYMENT_NAME --namespace=$NAMESPACE --timeout=5m

echo ""
echo -e "${GREEN}✅ Deployment Complete!${NC}"
echo ""

# Get service info
echo "Service Information:"
kubectl get service $DEPLOYMENT_NAME --namespace=$NAMESPACE

echo ""
echo "Pod Information:"
kubectl get pods --namespace=$NAMESPACE -l app=$DEPLOYMENT_NAME

echo ""
echo "View pod logs:"
echo "  kubectl logs -f pod/nursing-validator-xxx --namespace=$NAMESPACE"
echo ""
echo "Port forward for local access:"
echo "  kubectl port-forward svc/$DEPLOYMENT_NAME 8501:80 --namespace=$NAMESPACE"
echo ""
echo "Access from outside cluster:"
EXTERNAL_IP=$(kubectl get service $DEPLOYMENT_NAME --namespace=$NAMESPACE -o jsonpath='{.status.loadBalancer.ingress[0].ip}' 2>/dev/null || echo "PENDING")
if [ "$EXTERNAL_IP" != "PENDING" ]; then
  echo -e "${GREEN}http://$EXTERNAL_IP:8501${NC}"
else
  echo "Waiting for LoadBalancer IP..."
  echo "Run: kubectl get service $DEPLOYMENT_NAME --namespace=$NAMESPACE"
fi
