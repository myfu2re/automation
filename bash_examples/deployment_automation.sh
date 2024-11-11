#!/bin/bash

REPO_DIR="/path/to/your/repo"
SERVICE_NAME="your-service-name"

echo "Updating code in $REPO_DIR..."
cd "$REPO_DIR" || exit
git pull origin main

if [ $? -eq 0 ]; then
    echo "Code updated successfully."
else
    echo "Error updating code from Git."
    exit 1
fi

echo "Restarting service $SERVICE_NAME..."
sudo systemctl restart "$SERVICE_NAME"

if [ $? -eq 0 ]; then
    echo "Service $SERVICE_NAME restarted successfully."
else
    echo "Error restarting service $SERVICE_NAME."
    exit 1
fi

echo "Checking service status $SERVICE_NAME..."
sudo systemctl status "$SERVICE_NAME"
