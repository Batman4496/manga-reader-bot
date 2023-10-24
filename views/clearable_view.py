import discord
import discord.ui as UI

class Clearable:

  async def clear(self, interaction: discord.Interaction):
    await interaction.response.edit_message(content="Cleared", view=None, embed=None, delete_after=2)

  def clear_button(self, label = "Clear"):    
    button = UI.Button(style=discord.ButtonStyle.red, label="Clear")
    button.callback = self.clear

    return button
