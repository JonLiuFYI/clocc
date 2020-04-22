import os
import json

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

PREFIX = '⌚'

user_tzs = {}

clocc = commands.Bot(command_prefix=PREFIX,
                     description='Convert your time to other time zones')


@clocc.event
async def on_ready():
    print(f'{clocc.user.name} connected to Discord')
    with open('usertimezones.json', 'r') as f:
        global user_tzs
        user_tzs = json.load(f)


@clocc.command(name='time', help='Convert the given time')
async def convert_time(ctx, t: str, *tzs):
    await ctx.send(f'Time {t} in other time zones...')


@clocc.command(name='mytimezone', help='Set your time zone')
async def set_tz(ctx, t: str):
    user_tzs[str(ctx.author.id)] = t
    await ctx.send(f'{ctx.author}, your time zone has been set to **{t}**.')
    with open('usertimezones.json', 'w') as f:
        json.dump(user_tzs, f)


@clocc.command(name='target', help='Set what time zones this bot will convert to by default')
async def set_target(ctx, *tzs):
    await ctx.send('Not implemented yet!')


clocc.run(token)
