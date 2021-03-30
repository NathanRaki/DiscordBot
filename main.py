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

f = open("token.txt", "r")

client.run(f.read())