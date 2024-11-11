#!/bin/bash

SOURCE_DIR="/path/to/source"
BACKUP_DIR="/path/to/backup"
DATE=$(date +%Y-%m-%d_%H-%M-%S)
BACKUP_FILE="backup_$DATE.tar.gz"

echo "Creating a backup copy $SOURCE_DIR..."
tar -czf "$BACKUP_DIR/$BACKUP_FILE" "$SOURCE_DIR"

if [ $? -eq 0 ]; then
    echo "Backup completed successfully! File saved as $BACKUP_DIR/$BACKUP_FILE"
else
    echo "An error occurred while creating a backup copy."
fi
