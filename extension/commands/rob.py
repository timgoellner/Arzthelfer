import nextcord
from nextcord.ext import commands

from colorama import Fore
import datetime

import random
import json

class rob(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def rob(self, ctx, user : commands.MemberConverter()):
        try:
            with open("", "r") as data_file:
                data = json.load(data_file)

            try: 
                can_rob = data["economy"]["rob"][str(ctx.author.id)]
                if can_rob == False:
                    await ctx.send("```❌ Du kannst noch nicht wieder jemanden ausrauben```")
                    return
            except:
                data["economy"]["rob"][str(ctx.author.id)] = True
                with open("", "w") as data_file:
                    json.dump(data, data_file, indent=4)

            try:
                if data["economy"]["money"][str(user.id)] == 0: has_money = False
                else: has_money = True
            except: has_money = False

            if not has_money:
                await ctx.send(f"```❌ Der User {user} hat kein Geld```")
                return

            if random.randint(1, 5) != 1:
                member_minus_money = random.randint(1, int(data["economy"]["money"][str(ctx.author.id)] / 4))
                member_money = data["economy"]["money"][str(ctx.author.id)] - member_minus_money
                data["economy"]["money"][str(ctx.author.id)] = member_money

                await ctx.send(f"```👤💰 Du wurdest beim ausrauben erwischt und musst {member_minus_money}💵 zahlen```")

                data["economy"]["rob"][str(ctx.author.id)] = False

                with open("", "w") as data_file:
                    json.dump(data, data_file, indent=4)
                return

            member_plus_money = random.randint(int(data["economy"]["money"][str(user.id)] * 0.75), int(data["economy"]["money"][str(user.id)] * 0.9))
            member_money = data["economy"]["money"][str(ctx.author.id)] + member_plus_money
            user_money = data["economy"]["money"][str(user.id)] - member_plus_money
            data["economy"]["money"][str(ctx.author.id)] = member_money
            data["economy"]["money"][str(user.id)] = user_money

            await ctx.send(f"```💎💰 Du konntest {member_plus_money}💵 von {user} stehlen```")

            data["economy"]["rob"][str(ctx.author.id)] = False

            with open("", "w") as data_file:
                json.dump(data, data_file, indent=4)

        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Command {Fore.CYAN}rob{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

def setup(client):
    client.add_cog(rob(client))
