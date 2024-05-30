import discord
from discord.ext import commands


class Lockdown(commands.Cog): 
  
  def __init__(self, bot: discord.Bot):
    self.bot = bot

  @discord.slash_command(name="lockdown", description="LOCKDOWN! LOCKDOWN! THE WHOLE CITY IS SHUTDOWN!")
  async def lockdown(
      self, 
      ctx: discord.ApplicationContext, 
  ):
    await ctx.response.defer()
    author: discord.Member = ctx.author
    print(author.guild_permissions)
    
    if not author.guild_permissions.administrator:
      return await ctx.followup.send("Nuh uh.")

    return await ctx.followup.send("ok.")
  
def setup(bot):
  bot.add_cog(Lockdown(bot))