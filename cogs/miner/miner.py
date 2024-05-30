import os
import discord
from discord.ext import commands
from constants import BONEMAN
 
class Miner(commands.Cog): 
  
  def __init__(self, bot: discord.Bot):
    self.bot = bot

  @discord.slash_command(name="mine-channel", description="Mines the channel in which this command is called.")
  async def mine(
      self, 
      ctx: discord.ApplicationContext, 
  ):
    if ctx.author.id != BONEMAN:
      return await ctx.send("Nuh uh. You can't do that!")
    
    msg = await ctx.send("Wait...")

    file = open(f"./storage/mine-channels/{ctx.channel.id}.txt", 'w')
    file.write("message_id,channel_id,author_id,username,message_content,created_at\n")
    file.close()

    file = open(f"./storage/mine-channels/{ctx.channel.id}.txt", 'a', encoding='utf-8')
    
    channel_history = ctx.channel.history(limit=None)

    async for message in channel_history:
      file.write(f'"{message.id}","{ctx.channel.id}","{message.author.id}","{message.author.name}","{message.content}","{message.created_at}"\n')
    file.close()

    attachment = discord.File(f"./storage/mine-channels/{ctx.channel.id}.txt")
    await msg.edit("Done.", file=attachment)    


def setup(bot):
  bot.add_cog(Miner(bot))