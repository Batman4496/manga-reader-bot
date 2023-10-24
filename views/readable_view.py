import discord
import discord.ui as UI
from views.page_reader_view import PageReaderView

class ReadableView:
  def __init__(self, manga, module):
    self.manga = manga
    self.module = module
    
  async def read_callback(self, interaction: discord.Interaction):
    await interaction.response.defer()
    view = PageReaderView(self.manga, self.module)
    embed, file = view.generate_embed()
    
    await interaction.followup.send(view=view.generate_view(), embed=embed, file=file)

  def read_button(self, disabled = False):    
    read = UI.Button(label="Read", disabled=disabled)
    read.callback = self.read_callback
    
    return read
  
  def generate_view(self):
    view = UI.View(self.read_button())
    return view
