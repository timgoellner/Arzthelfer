import nextcord
from nextcord.ext import commands

import json

from colorama import Fore
import datetime

class remove_item(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def remove_item(self, ctx, member : commands.MemberConverter, item : str):
        try:
            if not ctx.author.guild_permissions.administrator:
                await ctx.send(f"```❌ Du hast keine Rechte für diesen Command```")
                return

            with open("", "r") as data_file:
                data = json.load(data_file)

            item = item.lower()

            if not (member.id in data["economy"]["items"][item]["users"]):
                await ctx.send(f"```❌ {member} hat das Item {item} nicht```")
                return

            role = ctx.guild.get_role(data["economy"]["items"][item]["role"])
            data["economy"]["items"][item]["users"].remove(member.id)
            data["economy"]["items"][item]["collect"].pop(str(member.id)) 
            await member.remove_roles(role)

            with open("", "w") as data_file:
                data = json.dump(data, data_file, indent=4)

            await ctx.send(f"```📉 Dem User {member} wurde das Item {item} entfernt```")
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Command {Fore.CYAN}remove_item{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

def setup(client):
    client.add_cog(remove_item(client))
