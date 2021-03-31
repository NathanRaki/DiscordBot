import discord
from discord.ext import commands
from datetime import datetime, date

import re

class MakeCall(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['call'])
    async def makecall(self, ctx, *, args=None):
        gamesfile = open('games.txt', 'r')
        games = gamesfile.readlines()
        if not args:
            output = f'*To make a call type $call <gameid> <time> [description]*\n'
            output += '*Time format : HH:MM*\n'
            output += f'*Here is the list of available games :*\n'
            output += '```'
            for i in range(len(games)):
                game = games[i].split(';')[0]
                output += f'[{i}] {game}\n'
            output += '```'
            output += '*If your game is not in the list, type $addgame <gamename>*'
            await ctx.send(output)
            return
        args = args.split(' ')
        try:
            rolename = games[int(args[0])].split(';')[1]
            rolename = re.sub('[^A-Za-z0-9 ]+', '', rolename)
            role = discord.utils.get(ctx.guild.roles, name=rolename)
        except Exception:
            await ctx.send('*You entered a wrong gameid, please type **$call** to see the game list.*')
            return
        try:
            hour = datetime.strptime(args[1], '%H:%M')
        except Exception:
            await ctx.send('*You entered a wrong hour, please use HH:MM format (Example: 21:30)*')
            return
        now = date.today()
        time = hour.replace(day=now.day, month=now.month, year=now.year)
        time_str = time.strftime('%d/%m/%y %H:%M')
        description = ' '.join(args[2:])
        if not description:
            description = 'No description'
        with open('calls.txt', 'a', encoding='utf-8') as file:
            file.write(f'{args[0]};{time_str};{description}\n')
            n_lines = sum(1 for line in open('calls.txt'))
        output = '~~-----------------------~~\n'
        output += f'*<@{ctx.message.author.id}> has created a call !\n<@&{role.id}>*\n'

        gamename = games[int(args[0])].split(';')[0]
        output += f'> Game:             {gamename}\n'
        output += f'> Time:              {time_str}\n'
        output += f'> Description:  {description}\n'
        await ctx.send(output)

    @commands.command()
    async def addgame(self, ctx, *, game=None):
        if not game:
            await ctx.send('*Please enter a game name.*')
            return
        with open('games.txt', 'a') as file:
            file.write('\n'+game)
        await ctx.send(f'*The game {game} has been added to the list !*')
        
    @commands.command(aliases=['call?'])
    async def display_call(self, ctx):
        callsfile = open('calls.txt', 'r', encoding='utf-8')
        calls = callsfile.readlines()
        gamesfile = open('games.txt', 'r')
        games = gamesfile.readlines()
        for i in range(len(games)):
            games[i] = games[i].split(';')
        dates = []
        for i in range(len(calls)):
            calls[i] = calls[i].split(';')
            dates.append(calls[i][1])
            dates[i] = datetime.strptime(dates[i], '%d/%m/%y %H:%M')
        now = datetime.now()
        try:
            closest = min(date for date in dates if date > now)
        except Exception:
            await ctx.send('Sorry bro, looks like there\'s currently no call. But you can make one (type $call for info)')
            return
        callid = dates.index(closest)
        description = re.sub('\n', '', calls[callid][2])
        output = '**Next call**:\n'
        output += f'> Game:             *{games[int(calls[callid][0])][0]}*\n'
        output += f'> Time:              *{calls[callid][1]}*\n'
        output += f'> Description:  *{description}*\n'
        await ctx.send(output)

def setup(client):
    client.add_cog(MakeCall(client))