import discord
import discord.ui as UI
from helpers import get_key, get_image
from views.clearable_view import Clearable 
from views.readable_view import ReadableView

class SearchView(Clearable):
  def __init__(self, mangas: list[dict], source: str, module) -> None:
    self.mangas = mangas
    self.source = source
    self.module = module
    self.manga = None

  def get_options(self) -> list[discord.SelectOption]:
    return [
      discord.SelectOption(label=option['title'][:50], value=str(index))
      for index, option in enumerate(self.mangas)
    ]

  async def select_callback(self, interaction: discord.Interaction):
    await interaction.response.defer()
    value = int(interaction.data['values'][0])
    url = self.mangas[value].get('url')
    try:
      manga = self.module.get_manga(url)
      self.manga = manga 

      embed = discord.Embed(title=manga['title'])
      embed.add_field(name="Synopsis", value=f"{manga['description'][:500]}...", inline=False)
      embed.add_field(name="Author", value=manga['author'])
      embed.add_field(name="Total Chapters", value=len(manga.get('chapters') or []))
      embed.add_field(name="Genres", value=manga.get('genres'), inline=False)
      embed.add_field(name="URL", value=url)
      embed.set_footer(text="Try `/read` command to read a manga")
      file = discord.File(
        get_image(manga.get('image'), self.module.get_url()), 
        'manga-cover.jpg'
      )
      embed.set_image(url=f"attachment://manga-cover.jpg")
      
      await interaction.followup.send(view=self.generate_view(), embed=embed, file=file)

    except Exception as e:
      print(e)
      embed = discord.Embed(title="An Error Occured!")
      embed.add_field(name="Please try again with something else...", value=f"Error fetching details of **{url}**")
      
      await interaction.followup.send(embed=embed)

  def generate_embed(self, label = None):
    embed = discord.Embed(title=label)
    return embed

  def generate_view(self):
    select = UI.Select(
      options=self.get_options(),
      placeholder="Select a manga..."
    )

    read = ReadableView(self.manga, self.module)
    read_button = read.read_button(False if self.manga else True)
    select.callback = self.select_callback

    view = UI.View(select, read_button, self.clear_button(), timeout=30.0)
    return view