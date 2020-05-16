import os
import time
from discord.ext import commands

token = os.getenv('KING_TOKEN')

reaction_counter = 0 
every_num_messages = 5

# id of user to be crowned 
emoji = '👑'

bot = commands.Bot(".")

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to discord!')

@bot.event
async def on_message(message):
    global reaction_counter
    king_id = message.guild.owner_id
    if king_id == message.author.id:
        if reaction_counter % every_num_messages == 0:
            await message.add_reaction(emoji)
        reaction_counter += 1


bot.run(token)
