import discord
from discord.ext import commands

import random

class Draw(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def draw(self, ctx):
        await ctx.send(f'Congratulations <@{random.choice(ctx.message.mentions).id}>, you won the draw!')

def setup(client):
    client.add_cog(Draw(client))