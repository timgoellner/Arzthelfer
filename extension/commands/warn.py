import nextcord
from nextcord.ext import commands

import json

from colorama import Fore
import datetime

class warn(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def warn(self, ctx, member : commands.MemberConverter, *, reason = "Keine"):
        try:
            with open("", "r") as data_file:
                data = json.load(data_file)

            try:
                warns = data["moderation"]["warns"][str(member.id)]
                data["moderation"]["warns"][str(member.id)] = warns+1
            except:
                data["moderation"]["warns"][str(member.id)] = 1
                warns = 0

            with open("", "w") as data_file:
                json.dump(data, data_file, indent=4)

            warns += 1
            await ctx.send(f"```⚠️ {member} wurde gewarnt, er hat nun {warns} Verwarnungen\n📃 Begründung: {reason}```")
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Command {Fore.CYAN}warn{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

def setup(client):
    client.add_cog(warn(client))
