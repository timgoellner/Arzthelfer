import nextcord
from nextcord.ext import commands

import json

from colorama import Fore
import datetime

class set_money(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def set_money(self, ctx, member : commands.MemberConverter, money : str):
        try:
            if not ctx.author.guild_permissions.administrator:
                await ctx.send(f"```❌ Du hast keine Rechte für diesen Command```")
                return
            with open("", "r") as data_file:
                data = json.load(data_file)

            try:
                user_money = data["economy"]["money"][str(member.id)]
            except:
                data["economy"]["money"][str(member.id)] = 0
                user_money = 0

            if money.startswith('+'):
                user_money += int(money[1:])
                msg = f"📈 Dem User {member} wurden {money[1:]}💵 hinzugefügt"
            elif money.startswith('-'):
                user_money -= int(money[1:])
                msg = f"📉 Dem User {member} wurden {money[1:]}💵 entfernt"
            else:
                user_money = int(money)
                msg = f"💰 Das Geld von {member} wurde auf {money}💵 gesetzt"

            if str(user_money).startswith('-'): user_money = 0

            data["economy"]["money"][str(member.id)] = user_money

            with open("", "w") as data_file:
                data = json.dump(data, data_file, indent=4)

            await ctx.send(f"```{msg}```")
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Command {Fore.CYAN}set_money{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

def setup(client):
    client.add_cog(set_money(client))
