import nextcord
from nextcord.ext import commands

import json
import random

from colorama import Fore
import datetime

class xp_add(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, msg):
        try:
            with open("", "r") as data_file:
                data = json.load(data_file)

            if msg.author.bot: return

            if str(msg.author.id) not in data["xp"]: author_xp = 0
            else: author_xp = data["xp"][str(msg.author.id)]

            if random.randint(1, 2) == 1: return

            data["xp"][str(msg.author.id)] = author_xp + random.randint(5, 20)

            with open("", "w") as data_file:
                data = json.dump(data, data_file, indent=4)
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Event {Fore.CYAN}xp_add{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

def setup(client):
    client.add_cog(xp_add(client))