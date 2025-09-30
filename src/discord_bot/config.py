"""Configuration management with YAML and schema validation."""

import os
import yaml
from pathlib import Path
from typing import Optional
from pydantic import BaseModel, Field, validator
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class BotConfig(BaseModel):
    """Bot configuration schema."""
    
    name: str = Field(default="Discord Bot", description="The name of the bot")
    token: Optional[str] = Field(default=None, description="Discord bot token")
    sync_commands: bool = Field(default=True, description="Whether to sync slash commands on startup")
    
    @validator('token', pre=True, always=True)
    def get_token(cls, v):
        """Get token from config or environment variable."""
        if v is not None:
            return v
        # Fallback to environment variable
        token = os.getenv('DISCORD_TOKEN')
        if not token:
            raise ValueError("Discord token must be provided either in config.yml or DISCORD_TOKEN environment variable")
        return token


def load_config(config_path: str = "config.yml") -> BotConfig:
    """Load configuration from YAML file with schema validation."""
    config_file = Path(config_path)
    
    if not config_file.exists():
        # Create default config file
        default_config = {
            'name': 'Discord Bot',
            'sync_commands': True,
            # Token will be loaded from environment
        }
        
        with open(config_file, 'w') as f:
            yaml.safe_dump(default_config, f, default_flow_style=False)
        
        print(f"Created default config file: {config_path}")
    
    # Load config from file
    with open(config_file, 'r') as f:
        config_data = yaml.safe_load(f) or {}
    
    return BotConfig(**config_data)