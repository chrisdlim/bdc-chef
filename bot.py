import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv
from discord_bot import DiscordBot

print('Initializing bdc-chef...')

load_dotenv()
TOKEN = os.getenv('TOKEN')
EASTER_EGG_NAMES = os.getenv('EASTER_EGG_NAMES').split(',')

intents = discord.Intents.default()
intents.members = True

bot = DiscordBot(easter_egg_names=EASTER_EGG_NAMES)

@bot.command(name='let-him-cook')
async def let_him_cook(ctx: commands.Context):
  author = ctx.author
  chatroom = ctx.channel
  vc = author.voice

  if (vc):
    current_vc_users = vc.channel.members
  
    if len(current_vc_users):
      selected_user = random.choice(current_vc_users)
      msg = bot.get_chefs_message(selected_user)
      await bot.send(chatroom, msg)
  else:
    await bot.send(chatroom, "There's nobody here to cook. Is it...WET in here??")

bot.run(TOKEN)