import nextcord
from nextcord.ext import commands

import json

from colorama import Fore
import datetime

class help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        try:
            with open("", "r") as data_file:
                data = json.load(data_file)

            msg = "      📰 Hilfe Menu\n"
            for group in data["help"]:
                msg += f"\n   📋 Gruppe : {group}\n"
                for command in data["help"][group]:
                    msg += f"📎 {command}\n"

            await ctx.send(f"```{msg}```")
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Command {Fore.CYAN}help{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

def setup(client):
    client.add_cog(help(client))
