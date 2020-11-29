import discord
from discord.ext import commands
import json

client = commands.Bot(command_prefix='!')
client.remove_command("help")  # This needs for custom help command
__version__ = "0.3.2.1b"  # Version


@client.event
async def on_ready():
    # Changing bot status
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Activity(name=f"version {__version__} | !help",
                                                           url="https://www.twitch.tv/eds52",
                                                           type=discord.ActivityType.watching))
    print("Bot is ready.")


@client.event
async def on_command_error(ctx, error):
    # Ignoring CommandNotFound error

    if error == discord.ext.commands.errors.CommandNotFound:
        pass


# Cogs list
cogs = {"information", "8ball", "giveaway", "avatar", "moderation", "other", "dev"}

# Loading cogs
for cog in cogs:
    client.load_extension(f"cogs.{cog}")

# Authorizing the bot
with open("config.json", "r") as f:
    data = json.load(f)
token = data["token"]
client.run(str(token))
