import discord
from discord.ext import commands
from constants import sources, CHOICES
from views.search_view import SearchView
from classes.manga_manager import MangaManger

class Hot(commands.Cog): 
  
  def __init__(self, bot):
    self.bot = bot
    self.manager = MangaManger()

  @discord.slash_command(name="hot", description="Hot mangas")
  async def hot(
      self, 
      ctx: discord.ApplicationContext, 
      source: discord.Option(
        str, 
        description="Sources to search on", 
        choices=CHOICES      
      )
  ):
    await ctx.response.defer()
    module = self.manager.driver(source)
    manga_list = module.get_hot_mangas()

    view = SearchView(manga_list, source, module)

    return await ctx.followup.send(embed=view.generate_embed("Hot Mangas"), view=view.generate_view())

def setup(bot):
  bot.add_cog(Hot(bot))