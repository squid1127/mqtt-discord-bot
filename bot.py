#!/usr/bin/env python3
"""
Ultra simple Discord.py bot that reads token from .env file.
"""

import os
import logging
from dotenv import load_dotenv
import discord
from discord.ext import commands

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Bot configuration
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

if not DISCORD_TOKEN:
    logger.error("DISCORD_TOKEN not found in environment variables. Please check your .env file.")
    exit(1)

# Create bot instance with command prefix
intents = discord.Intents.default()
intents.message_content = True  # Required for message content access
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    """Event triggered when the bot is ready."""
    logger.info(f'{bot.user} has connected to Discord!')
    logger.info(f'Bot is in {len(bot.guilds)} guild(s)')


@bot.event
async def on_message(message):
    """Event triggered on every message."""
    # Don't respond to self
    if message.author == bot.user:
        return
    
    # Process commands
    await bot.process_commands(message)


@bot.command(name='ping')
async def ping(ctx):
    """Simple ping command to test bot functionality."""
    await ctx.send('Pong!')


@bot.command(name='hello')
async def hello(ctx):
    """Simple hello command."""
    await ctx.send(f'Hello, {ctx.author.mention}!')


def main():
    """Main function to run the bot."""
    try:
        logger.info("Starting Discord bot...")
        bot.run(DISCORD_TOKEN)
    except discord.LoginFailure:
        logger.error("Invalid Discord token. Please check your DISCORD_TOKEN in .env file.")
    except KeyboardInterrupt:
        logger.info("Bot stopped by user.")
    except Exception as e:
        logger.error(f"An error occurred: {e}")


if __name__ == '__main__':
    main()