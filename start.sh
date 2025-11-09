#!/bin/bash

# Brew View - Startup Script
# This script installs dependencies and starts the Flask application

echo "================================================"
echo "       Brew View - Potion Flow Monitoring      "
echo "================================================"
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed."
    echo "Please install Python 3.7 or higher to continue."
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"
echo ""

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ Error: pip3 is not installed."
    echo "Please install pip3 to continue."
    exit 1
fi

echo "✓ pip3 found: $(pip3 --version)"
echo ""

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv .venv
    if [ $? -eq 0 ]; then
        echo "✓ Virtual environment created successfully"
    else
        echo "❌ Failed to create virtual environment"
        exit 1
    fi
else
    echo "✓ Virtual environment already exists"
fi
echo ""

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source .venv/bin/activate
if [ $? -eq 0 ]; then
    echo "✓ Virtual environment activated"
else
    echo "❌ Failed to activate virtual environment"
    exit 1
fi
echo ""

# Install/upgrade pip
echo "📦 Upgrading pip..."
pip install --upgrade pip --quiet
echo ""

# Install dependencies
echo "📦 Installing dependencies from requirements.txt..."
pip install -r requirements.txt
if [ $? -eq 0 ]; then
    echo "✓ Dependencies installed successfully"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi
echo ""

# Start Flask application
echo "================================================"
echo "🚀 Starting Brew View application..."
echo "================================================"
echo ""
echo "The application will be available at:"
echo "   http://localhost:5000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python flask_app.py
