import discord
from views.clearable_view import Clearable
from views.readable_view import ReadableView
import discord.ui as UI
from helpers import get_image
from views.page_reader_view import PageReaderView

class ReaderView(Clearable):
  def __init__(self, manga, module):
    self.manga = manga
    self.module = module
  
  async def read_callback(self, interaction: discord.Interaction):
    await interaction.response.defer()
    view = PageReaderView(self.manga, self.module)
    embed, file = view.generate_embed()
    
    message: discord.InteractionMessage = await interaction.original_response()
    await interaction.followup.edit_message(message_id=message.id, view=view.generate_view(), embed=embed, file=file)

  def generate_embed(self) -> (discord.Embed, discord.File):
    manga = self.manga
    embed = discord.Embed(title=manga['title'])
    embed.add_field(name="Synopsis", value=f"{manga['description'][:500]}...", inline=False)
    embed.add_field(name="Author", value=manga['author'])
    embed.add_field(name="Total Chapters", value=len(manga.get('chapters') or []))
    embed.add_field(name="Genres", value=manga.get('genres'), inline=False)
    embed.add_field(name="URL", value=manga.get('url'))
    image = get_image(manga.get('image'), self.module.get_url())
    file = discord.File(image, 'manga-cover.jpg')
    embed.set_image(url=f"attachment://manga-cover.jpg")

    return embed, file

  def generate_view(self) -> UI.View:
    read = ReadableView(self.manga, self.module)
    view = UI.View(read.read_button(), self.clear_button())

    return view