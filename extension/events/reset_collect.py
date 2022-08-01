import nextcord
from nextcord.ext import commands

import json

from colorama import Fore
import datetime

import asyncio

class reset_collection(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        try:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.MAGENTA}STARTED{Fore.RESET}] Started Economy Collection Resetting{Fore.LIGHTBLACK_EX}")

            while True:
                with open("", "r") as data_file:
                    data = json.load(data_file)

                for item in data["economy"]["items"]:
                    for user in data["economy"]["items"][item]["collect"]:
                        if data["economy"]["items"][item]["collect"][user] == False:
                            data["economy"]["items"][item]["collect"][user] = True

                channel = self.client.get_channel(data["economy"]["collect_channel"])
                await channel.send("```🤑 Alle Belohnungen können wieder abgeholt werden```")

                with open("", "w") as data_file:
                    data = json.dump(data, data_file, indent=4)

                await asyncio.sleep(86400)
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Event {Fore.CYAN}reset_collection{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

def setup(client):
    client.add_cog(reset_collection(client))
