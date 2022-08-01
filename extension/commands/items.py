import nextcord
from nextcord.ext import commands

import json

from colorama import Fore
import datetime

class items(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def items(self, ctx):
        try:
            with open("", "r") as data_file:
                data = json.load(data_file)

            msg = f"     - Alle Kaufbaren Items/Ränge -\n\n"
            for item in data["economy"]["items"]:
                price = data["economy"]["items"][item]["price"]
                money = data["economy"]["items"][item]["money"]
                msg += f"📜 Rolle: {item}\n   💰 Kaufpreis: {price}💵\n   📦 Auto Geld: {money}💵\n\n"

            await ctx.send(f"```{msg}```")
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Command {Fore.CYAN}items{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

def setup(client):
    client.add_cog(items(client))
