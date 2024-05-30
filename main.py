import discord
from discord.ext import bridge
import os # default module
# from dotenv import load_dotenv
from constants import COGS

# load_dotenv() # load all the variables from the env file

intents = discord.Intents()
intents.message_content = True

bot = discord.Bot(command_prefix="~", intents=intents)

@bot.event
async def on_ready() -> None:
  print("READY!!!") 

@bot.slash_command(description="Say Hi!")
async def hello(ctx):
  await ctx.respond("Hello!")

for cog in COGS:
  bot.load_extension(f'cogs.{cog}')
  print(cog, "loaded!")

bot.run("OTM3MDAzMjQ2NjgwMTU4MjA4.GzESe3.y6JJBiUrhxkaA4tzCJPNg9JeqKjgZ6dr9Tj9nE") # run the bot with the token