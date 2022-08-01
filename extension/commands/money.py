import nextcord
from nextcord.ext import commands

import json

from colorama import Fore
import datetime

class money(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def money(self, ctx, member : commands.MemberConverter = None):
        try:
            with open("", "r") as data_file:
                data = json.load(data_file)

            if member == None: member = ctx.message.author

            try:
                money = data["economy"]["money"][str(member.id)]
            except:
                data["economy"]["money"][str(member.id)] = 0
                with open("", "w") as data_file:
                    data = json.dump(data, data_file, indent=4)
                money = 0

            await ctx.send(f"```💰 {member} hat {money}💵```")
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Command {Fore.CYAN}money{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

def setup(client):
    client.add_cog(money(client))
