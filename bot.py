import os
import time
from discord.ext import commands

token = os.getenv('KING_TOKEN')

every_num_messages = 5

# id of user to be crowned 
emoji = '👑'

bot = commands.Bot(".")

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to discord!')

@bot.event
async def on_message(message):
    reaction_counter = 0
    with open('reaction_counter.txt', 'r') as data_file:
        reaction_counter = int(data_file.read())
    king_id = message.guild.owner_id
    if king_id == message.author.id:
        if reaction_counter % every_num_messages == 0:
            await message.add_reaction(emoji)
        with open('reaction_counter.txt', 'w') as data_file:
            reaction_counter += 1
            data_file.write(reaction_counter)


bot.run(token)
