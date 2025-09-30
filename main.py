#!/usr/bin/env python3
"""Main entry point for the Discord bot."""

import sys
import logging
import asyncio
from pathlib import Path

# Add src directory to Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from discord_bot.config import load_config
from discord_bot.bot import DiscordBot


def setup_logging():
    """Configure logging."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler('bot.log', encoding='utf-8')
        ]
    )


async def main():
    """Main function to run the bot."""
    setup_logging()
    logger = logging.getLogger(__name__)
    
    try:
        # Load configuration
        config = load_config()
        logger.info(f"Loaded configuration for: {config.name}")
        
        # Create and run bot
        bot = DiscordBot(config)
        
        async with bot:
            await bot.start(config.token)
            
    except KeyboardInterrupt:
        logger.info("Bot stopped by user.")
    except Exception as e:
        logger.error(f"An error occurred: {e}", exc_info=True)
        sys.exit(1)


if __name__ == '__main__':
    asyncio.run(main())