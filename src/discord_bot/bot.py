"""Main Discord bot class."""

import logging
import discord
from discord.ext import commands
from .config import BotConfig

logger = logging.getLogger(__name__)


class DiscordBot(commands.Bot):
    """Main Discord bot class."""
    
    def __init__(self, config: BotConfig):
        """Initialize the bot with configuration."""
        self.config = config
        
        # Configure intents
        intents = discord.Intents.default()
        intents.message_content = True
        
        super().__init__(
            command_prefix='!',  # Keep for backwards compatibility, but we'll use app commands
            intents=intents,
            help_command=None  # Disable default help command
        )
    
    async def setup_hook(self):
        """Setup hook called when bot is starting up."""
        logger.info(f"Setting up {self.config.name}...")
        
        # Load command cogs
        await self.load_extension('discord_bot.commands.basic')
        
        # Sync slash commands if configured
        if self.config.sync_commands:
            logger.info("Syncing application commands...")
            await self.tree.sync()
            logger.info("Application commands synced!")
    
    async def on_ready(self):
        """Event triggered when bot is ready."""
        logger.info(f'{self.config.name} ({self.user}) has connected to Discord!')
        logger.info(f'Bot is in {len(self.guilds)} guild(s)')
        logger.info(f'Application commands: {len(await self.tree.fetch_commands())}')
    
    async def on_error(self, event, *args, **kwargs):
        """Handle errors."""
        logger.error(f'An error occurred in event {event}', exc_info=True)