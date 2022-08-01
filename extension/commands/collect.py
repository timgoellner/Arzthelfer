import nextcord
from nextcord.ext import commands

import json

from colorama import Fore
import datetime

class collect(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def collect(self, ctx):
        try:
            with open("", "r") as data_file:
                data = json.load(data_file)

            msg = ""
            money = 0
            items = 0

            for item in data["economy"]["items"]:
                if str(ctx.author.id) in data["economy"]["items"][item]["collect"]:
                    if data["economy"]["items"][item]["collect"][str(ctx.author.id)] == True:
                        role = ctx.guild.get_role(data["economy"]["items"][item]["role"])
                        gain = data["economy"]["items"][item]["money"]
                        msg += f" 💳 {role} >> {gain}💵\n"
                        items += 1
                        money += gain
                        data["economy"]["items"][item]["collect"][str(ctx.author.id)] = False

            if items == 0:
                await ctx.send("```❌ Du kannst noch nicht wieder eine Belohnung abholen```")
                return

            current_money = data["economy"]["money"][str(ctx.author.id)]
            data["economy"]["money"][str(ctx.author.id)] = current_money+money

            with open("", "w") as data_file:
                data = json.dump(data, data_file, indent=4)

            await ctx.send(f"```  🏦 Du konntest {items} Belohnungen für {money}💵 abholen\n\n{msg}```")
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Command {Fore.CYAN}collect{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

def setup(client):
    client.add_cog(collect(client))
