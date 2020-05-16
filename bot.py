import os
import time
from discord.ext import commands

token = os.getenv('KING_TOKEN')

# id of user to be crowned 
emoji = '👑'

bot = commands.Bot(".")

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to discord!')

@bot.event
async def on_message(message):
    king_id = message.guild.owner_id
    if king_id == message.author.id:
        await message.add_reaction(emoji)
        sleep(120)


bot.run(token)

