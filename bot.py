import os
import time
from discord.ext import commands

token = os.getenv('KING_TOKEN')

reaction_counters = {}
every_num_messages = 5

# id of user to be crowned 
emoji = '👑'

bot = commands.Bot(".")

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to discord!')

@bot.event
async def on_message(message):
    global reaction_counters
    king_id = message.guild.owner_id
    if king_id == message.author.id:
        if king_id not in reaction_counters:
            reaction_counters[king_id] = 0
        if reaction_counters[king_id] == 0:
            await message.add_reaction(emoji)
        reaction_counters[king_id] += 1
        if reaction_counters[king_id] == every_num_messages:
            reaction_counters[king_id] = 0


bot.run(token)
