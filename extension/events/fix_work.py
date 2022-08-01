import nextcord
from nextcord.ext import commands

import json

from colorama import Fore
import datetime

class fix_work(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        try:
            with open("", "r") as data_file:
                data = json.load(data_file)

            for user in data["economy"]["work"]:
                data["economy"]["work"][user] = True

            with open("", "w") as data_file:
                data = json.dump(data, data_file, indent=4)
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Event {Fore.CYAN}fix_work{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")
            
def setup(client):
    client.add_cog(fix_work(client))
