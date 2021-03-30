import discord
from discord.ext import commands

class OnMemberJoin(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member.name} ({member.id}) joined.')
        await ctx.message.channel.send(f'Salut bg <@{member.id}>, t\'es le bienvenue !')

def setup(client):
    client.add_cog(OnMemberJoin(client))