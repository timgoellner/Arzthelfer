import nextcord
from nextcord.ext import commands

from colorama import Fore
import datetime

import asyncio
import json

class reset_rob(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        try:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.MAGENTA}STARTED{Fore.RESET}] Started Robbing Resetting{Fore.LIGHTBLACK_EX}")

            while True:
                with open("", "r") as data_file:
                    data = json.load(data_file)

                for user in data["economy"]["rob"]:
                    if data["economy"]["rob"][user] == False:
                        data["economy"]["rob"][user] = True

                with open("", "w") as data_file:
                    data = json.dump(data, data_file, indent=4)

                data_file.close()

                await asyncio.sleep(1800)
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Event {Fore.CYAN}reset_rob{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

def setup(client):
    client.add_cog(reset_rob(client))
