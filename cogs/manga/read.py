import discord
from discord.ext import commands
from constants import CHOICES
from views.reader_view import ReaderView
from classes.manga_manager import MangaManger

class Read(commands.Cog): 
  
  def __init__(self, bot):
    self.bot = bot
    self.manager = MangaManger()

  @discord.slash_command(name="read", description="Read a manga")
  async def read(
      self, 
      ctx: discord.ApplicationContext,
      url: discord.Option(
        str,
        description="Url of manga."
      ), 
      source: discord.Option(
        str, 
        description="Sources to search on", 
        choices=CHOICES      
      )
  ):
    await ctx.response.defer()
    module = self.manager.driver(source)
    manga = module.get_manga(url)

    view = ReaderView(manga, module)
    embed, file = view.generate_embed()

    return await ctx.followup.send(embed=embed, view=view.generate_view(), file=file)

def setup(bot):
  bot.add_cog(Read(bot))