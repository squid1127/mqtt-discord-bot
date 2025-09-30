#!/bin/bash
# Development initialization script for Discord bot.
# Creates virtual environment, installs dependencies, and sets up basic configuration.

set -e  # Exit on any error

echo "🚀 Initializing Discord Bot Development Environment..."

# Check if Python 3.11+ is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "📋 Using Python $PYTHON_VERSION"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
else
    echo "📦 Virtual environment already exists"
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📚 Installing dependencies..."
pip install -r requirements.txt

# Create default config if it doesn't exist
if [ ! -f "config.yml" ]; then
    echo "⚙️  Creating default configuration..."
    cat > config.yml << EOF
# Discord Bot Configuration
name: "My Discord Bot"
sync_commands: true

# Token will be loaded from DISCORD_TOKEN environment variable
# Alternatively, you can uncomment and set it here (not recommended for production):
# token: "your_bot_token_here"
EOF
fi

# Create .env.example if it doesn't exist
if [ ! -f ".env.example" ]; then
    echo "📝 Creating .env example..."
    cat > .env.example << EOF
# Discord Bot Token
# Get your token from https://discord.com/developers/applications
DISCORD_TOKEN=your_discord_bot_token_here
EOF
fi

# Create .env if it doesn't exist
if [ ! -f ".env" ]; then
    echo "📝 Creating .env file from example..."
    cp .env.example .env
    echo "⚠️  Please edit .env and add your Discord bot token!"
fi

echo ""
echo "✅ Development environment initialized successfully!"
echo ""
echo "Next steps:"
echo "1. Edit .env and add your Discord bot token"
echo "2. Optionally edit config.yml to customize bot settings"
echo "3. Run the bot with: python main.py"
echo ""
echo "To activate the virtual environment in the future:"
echo "source venv/bin/activate"