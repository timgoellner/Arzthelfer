import nextcord
from nextcord.ext import commands

import json

from colorama import Fore
import datetime

import asyncio
import random

class roulette(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def roulette(self, ctx, bet : str, bid : str):
        try:
            with open("", "r") as data_file:
                data = json.load(data_file)

            if not (((bet == "red") or (bet == "black")) or (bet.isdigit() and ((int(bet) <= 36) and (int(bet) >= 0)))):
                await ctx.send(f"```❌ Du kannst nicht auf {bet} wetten, nur auf \"red\",\"black\",0-36```")
                return

            if bid == "all": bid = str(data["economy"]["money"][str(ctx.author.id)])

            if bid.startswith('-') or (not bid.isdigit()):
                await ctx.send(f"```❌ Du kannst nicht {bid} einsetzen, nur 1 bis ... 💵```")
                return

            bid = int(bid)

            if bid < 1:
                await ctx.send("```❌ Du musst mindestens 1💵 einsetzen```")
                return

            if bid > int(data["economy"]["money"][str(ctx.author.id)]):
                await ctx.send("```❌ Du hast nicht genug geld```")
                return

            msg = await ctx.send(f"```  - 🎰 Roulette Spiel von {ctx.author} -\n🎲 Wette : {bet}\n💸 Einsatz : {bid}💵\n\n🕹️ Ergebniss : ⏱️ Rolling...```")
            await asyncio.sleep(4)
            result = random.randint(0, 36)

            if result%2 == 0: win_result = f"red {result}"
            else: win_result = f"black {result}"

            if bet == "red" and win_result.split(" ")[0] == "red": win = "true"
            elif bet == "black" and win_result.split(" ")[0] == "black": win = "true"
            elif bet == str(result): win = "super"
            else: win = "false"

            if win == "true": win_sum = bid
            elif win == "super": win_sum = bid*36
            else: win_sum = -bid

            money = int(data["economy"]["money"][str(ctx.author.id)])
            data["economy"]["money"][str(ctx.author.id)] = (money + win_sum)

            with open("", "w") as data_file:
                data = json.dump(data, data_file, indent=4)

            if win == "true": result_emoji = '🏆'
            elif win == "false": result_emoji = '🚫'
            else: result_emoji = '🎯'

            await msg.edit(content=f"```  - 🎰 Roulette Spiel von {ctx.author} -\n🎲 Wette : {bet}\n💸 Einsatz : {bid}💵\n\n🕹️ Ergebniss : {win_result} ({result_emoji})\n💰 Money : {win_sum}💵```")
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Command {Fore.CYAN}roulette{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

def setup(client):
    client.add_cog(roulette(client))
