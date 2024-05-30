import discord
from discord.ext import commands
from constants import BONEMAN

class Chat(commands.Cog): 
  
  def __init__(self, bot):
    self.bot = bot

  @discord.slash_command(name="chat", description="Ask the AI.")
  async def chat(
      self, 
      ctx: discord.ApplicationContext, 
      question: discord.Option(
        str, 
        description="Question for the AI."
      )
  ):
    if ctx.author.id != BONEMAN:
      return await ctx.send("Nuh uh. You can't do that!")


def setup(bot):
  bot.add_cog(Chat(bot))