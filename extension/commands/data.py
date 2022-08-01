
import nextcord
from nextcord.ext import commands

import json

from colorama import Fore
import datetime

import requests

class data(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def data(self, ctx):
        try:
            if not ctx.author.guild_permissions.administrator:
                await ctx.send(f"```❌ Du hast keine Rechte für diesen Command```")
                return
                
            with open("", "rb") as data_file:
                await ctx.send(file=nextcord.File(data_file, "data.json"))
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Command {Fore.CYAN}data{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

def setup(client):
    client.add_cog(data(client))
