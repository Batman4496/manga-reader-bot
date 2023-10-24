import discord
from views.clearable_view import Clearable
import discord.ui as UI
from helpers import get_image


class PageReaderView(Clearable):
  def __init__(self, manga, module):
    self.manga = manga
    self.module = module
    self.chapter_list = manga.get('chapters')
    self.current_chapter = 0
    self.chapter = self.chapter_list[self.current_chapter]
    self.current_page = 0
    self.pages = None

  def get_options(self) -> list[dict]:
    chapters  = self.manga.get('chapters')
    start = self.current_chapter
    end = start + 20
    i = start
    options = []

    for chapter in chapters[start:end]:
      options.append(discord.SelectOption(label=chapter['title'][:50], value=str(i)))
      i += 1

    return options
  

  async def select_callback(self, interaction: discord.Interaction):
    await interaction.response.defer()
    value = int(interaction.data['values'][0])
    
    self.current_chapter = value
    self.chapter = self.chapter_list[value]
    self.pages = []
    self.current_page = 0

    embed, file = self.generate_embed()
    message: discord.InteractionMessage = await interaction.original_response()
    await interaction.followup.edit_message(message_id=message.id, view=self.generate_view(), embed=embed, file=file)
  
  def generate_embed(self) -> (discord.Embed, discord.File):   
    chapter = self.chapter
    if not self.pages:
      # Loading all chapter pages
      self.pages = self.module.get_chapter(chapter.get('url'))
  
    embed = discord.Embed(title="Reader...")
    embed.add_field(name=f"Chapter", value=f"{chapter.get('title')}")
    image = get_image(self.pages[self.current_page].get('image'), self.module.get_url())
    name = f"page-{self.current_page}.png"
    file = discord.File(image, name)
    embed.set_image(url=f"attachment://{name}")
    embed.set_footer(text=f"{self.current_page + 1}/{len(self.pages)}")

    return embed, file
  
  async def chapter_callback(self, interaction: discord.Interaction, next: bool):
    """ Gets the previous or next chapter """
    await interaction.response.defer()
    if next:
      # Next chapter
      if self.current_chapter == (len(self.chapter_list) - 1):
        self.current_chapter = 0
      else:
        self.current_chapter += 1
    else:
      # Previous chapter
      if self.current_chapter == 0:
        self.current_chapter = len(self.chapter_list) - 1
      else:
        self.current_chapter -= 1


    self.chapter = self.chapter_list[self.current_chapter]
    self.pages = []
    self.current_page = 0

    embed, file = self.generate_embed()
    message: discord.InteractionMessage = await interaction.original_response()
    await interaction.followup.edit_message(message_id=message.id, view=self.generate_view(), embed=embed, file=file)


  async def page_callback(self, interaction: discord.Interaction, next: bool):
    """ Gets the previous or next page of the current chapter """
    await interaction.response.defer()
    if next:
      # Next page
      if self.current_page == (len(self.pages) - 1):
        self.current_page = 0
      else:
        self.current_page += 1
    else:
      # Previous page page
      if self.current_page == 0:
        self.current_page = len(self.pages) - 1
      else:
        self.current_page -= 1
      
    embed, file = self.generate_embed()
    message: discord.InteractionMessage = await interaction.original_response()
    await interaction.followup.edit_message(message_id=message.id, view=self.generate_view(), embed=embed, file=file)


  def generate_view(self) -> UI.View:
    select = UI.Select(
      options=self.get_options(),
      placeholder="Select Chapter..."
    )

    select.callback = self.select_callback

    prev_page = UI.Button(label="◀")
    prev_page.callback = lambda interaction: self.page_callback(interaction, False)

    next_page = UI.Button(label="▶")
    next_page.callback = lambda interaction: self.page_callback(interaction, True)

    prev_chapter = UI.Button(label="⏪")
    prev_chapter.callback = lambda interaction: self.chapter_callback(interaction, False)

    next_chapter = UI.Button(label="⏩")
    next_chapter.callback = lambda interaction: self.chapter_callback(interaction, True)

    view = UI.View(prev_page, next_page, select, self.clear_button(), prev_chapter, next_chapter)
    return view