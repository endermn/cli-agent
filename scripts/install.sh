#!/bin/bash

# This script creates an executable for the termini Python script
# and installs it in /usr/local/bin.

set -e

# --- Configuration ---
EXECUTABLE_NAME="termini"
INSTALL_DIR="/usr/local/bin"
INSTALL_PATH="$INSTALL_DIR/$EXECUTABLE_NAME"


# --- Script ---

# This is assumed to be the project's root directory.
PROJECT_PATH=$(cd "$(dirname "$0")/.." && pwd)

echo "Project path detected: $PROJECT_PATH"
echo "Installing '$EXECUTABLE_NAME' to $INSTALL_PATH..."

SCRIPT_CONTENT="#!/bin/bash
cd \"$PROJECT_PATH\"
source .venv/bin/activate
python termini/main.py \"\$@\"
deactivate
cd - > /dev/null 2>&1
"

if [ ! -d "$INSTALL_DIR" ]; then
    echo "Installation directory $INSTALL_DIR does not exist."
    echo "Please create it or ensure it's in your system's PATH."
    exit 1
fi

# This is a safer way to write the file, especially when using sudo.
TEMP_FILE=$(mktemp)
echo "$SCRIPT_CONTENT" > "$TEMP_FILE"
chmod +x "$TEMP_FILE"

echo "You may be prompted for your password to install the script to $INSTALL_DIR."
sudo mv "$TEMP_FILE" "$INSTALL_PATH"
sudo chown "$(whoami)" "$INSTALL_PATH"

echo ""
echo "✅ Installation successful!"
echo ""
echo "You can now run '$EXECUTABLE_NAME' from anywhere in your terminal."
echo "Ensure '$INSTALL_DIR' is in your shell's PATH variable."
