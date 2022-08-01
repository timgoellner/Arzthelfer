import nextcord
from nextcord.ext import commands

import json

from colorama import Fore
import datetime

class warnlist(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def warnlist(self, ctx, member : commands.MemberConverter):
        try:
            with open("", "r") as data_file:
                data = json.load(data_file)

            try:
                warns = data["moderation"]["warns"][str(member.id)]
            except:
                warns = 0

            await ctx.send(f"```📜 {member} hat {warns} Verwarnungen```")
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Command {Fore.CYAN}warnlist{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

def setup(client):
    client.add_cog(warnlist(client))
