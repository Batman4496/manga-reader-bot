import discord
from discord.ext import commands
from constants import CHOICES
from views.search_view import SearchView
from classes.manga_manager import MangaManger

class Search(commands.Cog): 
    
    def __init__(self, bot):
      self.bot = bot
      self.manager = MangaManger()

    @discord.slash_command(name="search", description="Search a manga")
    async def search(
        self, 
        ctx: discord.ApplicationContext, 
        search: discord.Option(str, description="Managa You want to search"),
        source: discord.Option(
          str, 
          description="Sources to search on.", 
          choices=CHOICES,
          required=False,
          default=CHOICES[0]          
        )
    ):
      await ctx.response.defer()
      module = self.manager.driver(source)
      manga_list = module.search(search)
  
      view = SearchView(manga_list, source, module) 
      return await ctx.followup.send(embed=view.generate_embed(f"Search results for '{search}' on {source}"), view=view.generate_view())


def setup(bot):
  bot.add_cog(Search(bot))