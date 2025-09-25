import discord
from discord.ext import commands
import os
import asyncio
import logging
from dotenv import load_dotenv  # <-- import dotenv

intents = discord.Intents.default()
intents.message_content = True

# Optional logging to file
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

bot = commands.Bot(command_prefix="rp", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot logged in as {bot.user}")

async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    load_dotenv()  # Load variables from .env
    token = os.getenv("DISCORD_TOKEN")  # Read token
    async with bot:
        await load_cogs()
        await bot.start(token, log_handler=handler, log_level=logging.DEBUG)

asyncio.run(main())

