import os
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

for root, d_names, f_names in os.walk('./cogs/'):
    for filename in f_names:
        if filename.endswith('.py'):
            d = root[2:].replace('/','.')
            client.load_extension(f'{d}.{filename[:-3]}')
            print(f'Loaded {filename}')

client.run('ODI1ODg4NTI5OTU5MzU0NDA4.YGEeoQ.E018oFlGgyNOHlJqKQIG53iUkO4')