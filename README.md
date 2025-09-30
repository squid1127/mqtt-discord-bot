# mqtt-discord-bot

No, this is not done yet.

A "modular" discord.py-based MQTT bridge bot, designed to be somewhat feature-complete.

## Features

- Modern Discord bot using slash commands (app commands)
- YAML-based configuration with schema validation
- Modular structure ready for multiple files
- Environment-based token management
- Docker support with Python Alpine image
- Development initialization script
- Structured logging with file output

## Architecture

### Project Structure

```
mqtt-discord-bot/
├── src/discord_bot/          # Main bot package
│   ├── __init__.py          # Package initialization
│   ├── bot.py               # Main bot class
│   ├── config.py            # Configuration management
│   ├── commands/            # Command modules
│   │   ├── __init__.py
│   │   └── basic.py         # Basic commands (ping)
│   └── utils/               # Utility modules
├── scripts/
│   └── init.sh              # Development setup script
├── main.py                  # Entry point
├── requirements.txt         # Python dependencies
├── Dockerfile               # Docker container config
└── docker-compose.yml       # Docker orchestration
```

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

### Quick Start (Development)

1. Clone the repository:

   ```bash
   git clone https://github.com/squid1127/mqtt-discord-bot.git
   cd mqtt-discord-bot
   ```

2. Run the initialization script:

   ```bash
   ./scripts/init.sh
   ```

3. Edit `.env` and add your Discord bot token:

   ```env
   DISCORD_TOKEN=your_actual_bot_token_here
   ```

4. Optionally edit `config.yml` to customize bot settings:

   ```yaml
   name: "My Discord Bot"
   sync_commands: true
   ```

5. Run the bot:
   ```bash
   python main.py
   ```

### Manual Installation

#### Standalone (Python)

1. Create virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create configuration:

   ```bash
   cp .env.example .env
   # Edit .env with your token
   ```

4. Run the bot:
   ```bash
   python main.py
   ```

#### Docker

1. Create environment file:

   ```bash
   cp .env.example .env
   # Edit .env with your token
   ```

2. Build and run with Docker:

   ```bash
   docker build -t mqtt-discord-bot .
   docker run --env-file .env mqtt-discord-bot
   ```

   Or use docker-compose:

   ```bash
   docker-compose up --build
   ```

## Available Commands

- `/ping` - Check bot responsiveness and latency

## Configuration

### config.yml

```yaml
# Bot display name
name: "My Discord Bot"

# Whether to sync slash commands on startup
sync_commands: true
# Optional: Discord token (recommended to use .env instead)
# token: "your_token_here"
```

### Environment Variables (.env)

- `DISCORD_TOKEN` - Your Discord bot token (required)

## Development

### Adding New Commands

1. Create a new file in `src/discord_bot/commands/`
2. Implement your commands as a Cog with app commands
3. Add the extension loading in `src/discord_bot/bot.py`

Example command module:

```python
import discord
from discord.ext import commands

class MyCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="example", description="Example command")
    async def example(self, interaction: discord.Interaction):
        await interaction.response.send_message("Hello!")

async def setup(bot):
    await bot.add_cog(MyCommands(bot))
```

### Project Structure Benefits

- **Modular**: Easy to add new features in separate files
- **Scalable**: Ready for complex bot functionality
- **Maintainable**: Clear separation of concerns
- **Configurable**: YAML config with validation
- **Production-ready**: Docker support and proper logging

## License

MIT License - see [LICENSE](LICENSE) file for details.
