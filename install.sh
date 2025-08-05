#!/bin/bash

echo "=== TechJournal.it Automation Setup ==="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.7+ first."
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip first."
    exit 1
fi

echo "✅ pip3 found"

# Install dependencies
echo ""
echo "📦 Installing Python dependencies..."
pip3 install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed successfully"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

# Make the script executable
chmod +x techjournal_automation.py

echo ""
echo "✅ Setup completed successfully!"
echo ""
echo "To run the automation:"
echo "  python3 techjournal_automation.py"
echo ""
echo "To run in background:"
echo "  nohup python3 techjournal_automation.py > automation_output.log 2>&1 &"
echo ""
echo "To monitor logs:"
echo "  tail -f techjournal_automation.log"
echo ""
echo "To stop the automation:"
echo "  pkill -f techjournal_automation.py"