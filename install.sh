#!/bin/bash

# Set the path to the current working directory
SIMPLE_SITE_DIR="$(pwd)"

# Set the path to the target directory in /usr/local/bin
TARGET_BIN_DIR="/usr/local/bin"

# Set the path to the templates directory in /usr/local/share/simple_site
TARGET_SHARE_DIR="/usr/local/share/simple_site"

# Create the target directories if they don't exist
sudo mkdir -p "$TARGET_BIN_DIR"
sudo mkdir -p "$TARGET_SHARE_DIR"

# Copy the simple_site file to /usr/local/bin
sudo cp "$SIMPLE_SITE_DIR/simple_site" "$TARGET_BIN_DIR/simple_site"

# Set execute permissions for the simple_site file
sudo chmod +x "$TARGET_BIN_DIR/simple_site"

# Copy the templates directory to /usr/local/share/simple_site
sudo cp -r "$SIMPLE_SITE_DIR/templates" "$TARGET_SHARE_DIR"

echo "Installation complete. You can now run 'sudo simple_site --deploy' to deploy your application."
