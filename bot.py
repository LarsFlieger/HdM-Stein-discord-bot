import os
import asyncio
import discord
from dotenv import load_dotenv
from discord.ext import commands 

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix = "!")

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name="test",help="This is a test!")
async def on_message(ctx):
    await ctx.send("success")
    
bot.run(TOKEN)