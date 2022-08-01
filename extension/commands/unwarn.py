import nextcord
from nextcord.ext import commands

import json

from colorama import Fore
import datetime

class unwarn(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def unwarn(self, ctx, member : commands.MemberConverter):
        try:
            with open("", "r") as data_file:
                data = json.load(data_file)

            try:
                warns = data["moderation"]["warns"][str(member.id)]
                if warns == 0:
                    await ctx.send(f"```❌ {member} hat keine Verwarnungen```")
                    return

                data["moderation"]["warns"][str(member.id)] = 0
            except:
                await ctx.send(f"```❌ {member} hat keine Verwarnungen```")
                return

            with open("", "w") as data_file:
                json.dump(data, data_file, indent=4)

            await ctx.send(f"```📜 Die Verwarnunegn von {member} wurden entfernt```")
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Command {Fore.CYAN}unwarn{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

def setup(client):
    client.add_cog(unwarn(client))
