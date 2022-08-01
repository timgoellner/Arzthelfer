import nextcord
from nextcord.ext import commands

import json

from colorama import Fore
import datetime

class news(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def news(self, ctx):
        try:
            with open("", "r") as data_file:
                data = json.load(data_file)

            news_text = data["texts"]["news"]

            await ctx.send(f"```{news_text}```")
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Command {Fore.CYAN}news{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

def setup(client):
    client.add_cog(news(client))
