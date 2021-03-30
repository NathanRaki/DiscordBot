import discord
from discord.ext import commands

class OnMemberRemove(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member.name} ({member.id}) left.')
        await ctx.message.channel.send(f'Oh non ... <@{member.id}> nous a quitté ...')

def setup(client):
    client.add_cog(OnMemberRemove(client))