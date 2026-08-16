#!/bin/bash
set -e

# Change directory to the script's directory
cd "$(dirname "$0")"

echo "Creating python virtual environment in .venv..."
python3 -m venv .venv

echo "Upgrading pip..."
.venv/bin/pip install --upgrade pip

echo "Installing requirements..."
.venv/bin/pip install -r requirements.txt

echo "Environment setup complete!"
