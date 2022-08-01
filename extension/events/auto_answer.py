import nextcord
from nextcord.ext import commands

import json

from colorama import Fore
import datetime

class auto_answer(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, msg):
        try:
            with open("", "r") as data_file:
                data = json.load(data_file)

            if (msg.content in data["answer"]) and (not msg.author.bot):
                await msg.channel.send(data["answer"][msg.content])
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Event {Fore.CYAN}auto_answer{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

def setup(client):
    client.add_cog(auto_answer(client))
