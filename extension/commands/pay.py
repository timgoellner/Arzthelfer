import nextcord
from nextcord.ext import commands

import json

from colorama import Fore
import datetime

class pay(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def pay(self, ctx, member : commands.MemberConverter, money : str):
        try:
            with open("", "r") as data_file:
                data = json.load(data_file)

            if int(money) < 1:
                await ctx.send(f"```❌ Du kannst {member} nur 1 bis ...💵 geben```")
                return

            payer_money = data["economy"]["money"][str(ctx.author.id)]
            if member.id != 763414042979074068: reciever_money = data["economy"]["money"][str(member.id)]

            data["economy"]["money"][str(ctx.author.id)] = payer_money - int(money)
            if member.id != 763414042979074068: data["economy"]["money"][str(member.id)] = reciever_money + int(money)

            with open("", "w") as data_file:
                data = json.dump(data, data_file, indent=4)

            await ctx.send(f"```💳 Du hast {member} {money}💵 gegeben```")
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Command {Fore.CYAN}pay{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

def setup(client):
    client.add_cog(pay(client))
