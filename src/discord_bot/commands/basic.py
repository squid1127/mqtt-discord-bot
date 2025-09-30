"""Basic commands for the Discord bot."""

import logging
import discord
from discord.ext import commands

logger = logging.getLogger(__name__)


class BasicCommands(commands.Cog):
    """Basic command cog with app commands."""
    
    def __init__(self, bot):
        self.bot = bot
    
    @discord.app_commands.command(name="ping", description="Check if the bot is responding")
    async def ping(self, interaction: discord.Interaction):
        """Ping command to test bot responsiveness."""
        latency = round(self.bot.latency * 1000)
        embed = discord.Embed(
            title="🏓 Pong!",
            description=f"Bot latency: {latency}ms",
            color=discord.Color.green()
        )
        await interaction.response.send_message(embed=embed)
        logger.info(f"Ping command used by {interaction.user} in {interaction.guild}")


async def setup(bot):
    """Setup function to add the cog to the bot."""
    await bot.add_cog(BasicCommands(bot))