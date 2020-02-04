import os

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

PREFIX = '⌚'


class Clocc(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=PREFIX)

    async def on_ready(self):
        print(f'{self.user.name} has connected to Discord')

    async def on_message(self, message):
        if message.author == self.user.name:
            return

        if message.content == 'asdf':
            await message.channel.send('ASDF indeed')


bot = Clocc()
bot.run(token)
