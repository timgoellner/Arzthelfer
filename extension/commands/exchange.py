import nextcord
from nextcord.ext import commands

import json

from colorama import Fore
import datetime

class exchange(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def exchange(self, ctx, item : str):
        try:
            with open("", "r") as data_file:
                data = json.load(data_file)

            item = item.lower()

            try: data["economy"]["items"][item]
            except:
                await ctx.send(f"```❌ Item {item} konnte nicht gefunden werden```")
                return

            if not ctx.author.id in data["economy"]["items"][item]["users"]:
                await ctx.send(f"```❌ Du hast das item {item} nicht erworben```")
                return

            money = data["economy"]["money"][str(ctx.author.id)]
            price = data["economy"]["items"][item]["price"]

            role = ctx.guild.get_role(data["economy"]["items"][item]["role"])

            data["economy"]["money"][str(ctx.author.id)] = money+price
            await ctx.author.remove_roles(role)
            data["economy"]["items"][item]["users"].remove(ctx.author.id)
            data["economy"]["items"][item]["collect"].pop(str(ctx.author.id))

            with open("", "w") as data_file:
                data = json.dump(data, data_file, indent=4)

            await ctx.send(f"```🛒 Du hast das Item {item} für {price} zurückgegeben```")
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Command {Fore.CYAN}exchange{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

def setup(client):
    client.add_cog(exchange(client))
