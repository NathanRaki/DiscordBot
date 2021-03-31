import discord
from discord.ext import commands

import math
import random

class MakeTeams(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['mt'])
    async def maketeams(self, ctx, n_teams=None):
        mentions = ctx.message.mentions
        if not mentions:
            await ctx.send(f'*Please mention users you want to split in teams.*')
            return
        for i in range(len(mentions)):
            mentions[i] = mentions[i].name
        n_users = len(mentions)
        if not n_teams or not n_teams.isnumeric():
            await ctx.send(f'*No number of teams detected, assigning automatically...*')
            n_teams= int(n_users/round(math.sqrt(n_users)))
        else:
            n_teams = int(n_teams)
        number = 1
        while n_users > 0 and n_teams > 0:
            team = random.sample(mentions, int(n_users/n_teams))
            for user in team:
                mentions.remove(user)
            n_users -= int(n_users/n_teams)
            n_teams -= 1
            output = f'Team n°{number} :'
            for user in team:
                output += ' ' + user
            await ctx.send(output)
            number += 1

def setup(client):
    client.add_cog(MakeTeams(client))