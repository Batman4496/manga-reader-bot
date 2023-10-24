import discord
from discord.ext import commands


class Help(commands.Cog): 
  
  def __init__(self, bot):
    self.bot = bot

  @discord.slash_command(name="help", description="Tech support for bot")
  async def help(self, ctx):
    await ctx.response.defer()
    embed = discord.Embed(title="HELP SOMBODY HELP ME")
    embed.set_thumbnail(url=ctx.author.avatar)
    embed.add_field(name="Uhhh", value="Don't use MangaTown source as it is very slow", inline=False)
    embed.add_field(name="/search", value="Search a specific manga on sources")
    embed.add_field(name="/hot", value="Hot mangas")
    embed.add_field(name="/read", value="For reading a manga")

    embed.set_author(name="Hard as bone rn", url="https://discord.com/users/459250601314746375")

    await ctx.followup.send(embed=embed)

    
def setup(bot):
  bot.add_cog(Help(bot))