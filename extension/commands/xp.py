import nextcord
from nextcord.ext import commands

import json

from colorama import Fore
import datetime

class xp(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def xp(self, ctx, member : commands.MemberConverter = None):
        try:
            with open("", "r") as data_file:
                data = json.load(data_file)

            if member == None: member = ctx.author
            if str(member.id) not in data["xp"]:
                await ctx.send("❌ Der User hat keine XP")
                return
            
            author_xp = data["xp"][str(member.id)]

            await ctx.send(f"```🍀 Der User {member} hat {author_xp} XP```")
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Command {Fore.CYAN}xp{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

def setup(client):
    client.add_cog(xp(client))