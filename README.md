# mqtt-discord-bot
An ultra simple Discord.py bot that reads tokens from .env files. Can be run standalone or with Docker.

## Features
- Simple Discord bot with basic commands
- Environment-based configuration using .env files
- Docker support with Python Alpine image
- Basic logging and error handling

## Setup

### Prerequisites
- Python 3.11+ (for standalone) or Docker
- Discord bot token from [Discord Developer Portal](https://discord.com/developers/applications)

### Discord Bot Setup
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application
3. Go to the "Bot" section
4. Create a bot and copy the token
5. Enable "Message Content Intent" under "Privileged Gateway Intents"

### Installation

#### Standalone (Python)
1. Clone the repository:
   ```bash
   git clone https://github.com/squid1127/mqtt-discord-bot.git
   cd mqtt-discord-bot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create environment file:
   ```bash
   cp .env.example .env
   ```

4. Edit `.env` and add your Discord bot token:
   ```env
   DISCORD_TOKEN=your_actual_bot_token_here
   ```

5. Run the bot:
   ```bash
   python bot.py
   ```

#### Docker
1. Clone the repository:
   ```bash
   git clone https://github.com/squid1127/mqtt-discord-bot.git
   cd mqtt-discord-bot
   ```

2. Create environment file:
   ```bash
   cp .env.example .env
   ```

3. Edit `.env` and add your Discord bot token:
   ```env
   DISCORD_TOKEN=your_actual_bot_token_here
   ```

4. Build and run with Docker:
   ```bash
   docker build -t mqtt-discord-bot .
   docker run --env-file .env mqtt-discord-bot
   ```

   Or use docker-compose:
   ```bash
   docker-compose up --build
   ```

## Available Commands
- `!ping` - Responds with "Pong!"
- `!hello` - Greets the user

## Configuration
All configuration is done through environment variables in the `.env` file:

- `DISCORD_TOKEN` - Your Discord bot token (required)

## License
MIT License - see [LICENSE](LICENSE) file for details.
