import nextcord
from nextcord.ext import commands

from colorama import Fore
import datetime

import asyncio

class spam_clear(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        try:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.MAGENTA}STARTED{Fore.RESET}] Started Spam File Clearing{Fore.LIGHTBLACK_EX}")
            while True:
                with open("", "r+") as spam_file:
                    spam_file.truncate(0)
                await asyncio.sleep(10)
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Event {Fore.CYAN}spam_clear{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

def setup(client):
    client.add_cog(spam_clear(client))
