#!/bin/bash
# Local Deployment Script for Testing

set -e

echo "=== NHS Nursing Validator Phase 3 - Local Deployment ==="
echo ""

# Check Python
echo "Checking Python..."
python3 --version

# Create virtual environment
echo ""
echo "Creating virtual environment..."
python3 -m venv venv || true
source venv/bin/activate

# Install dependencies
echo ""
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Set environment variables
export $(cat .env.production | xargs)

# Run the application
echo ""
echo "Starting application..."
echo "Access at: http://localhost:8501"
echo ""

streamlit run app_phase2.py --logger.level=info
