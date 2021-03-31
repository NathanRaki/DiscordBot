import discord
from discord.ext import commands, tasks
from itertools import cycle

status = cycle(['Bored', 'Hyped', 'OMG'])

class OnReady(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        self.change_status.start()
        self.check_calls.start()
        print('Bot is ready.')

    @tasks.loop(seconds=10)
    async def change_status(self):
        await self.client.change_presence(activity=discord.Game(next(status)))

    @tasks.loop(seconds=10)
    async def check_calls(self):
        return

def setup(client):
    client.add_cog(OnReady(client))