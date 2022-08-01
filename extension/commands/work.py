import nextcord
from nextcord.ext import commands

import json

from colorama import Fore
import datetime

import asyncio
import random

class work(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def work(self, ctx):
        try:
            with open("", "r") as data_file:
                data = json.load(data_file)

            try:
                if data["economy"]["work"][str(ctx.author.id)] == False:
                    await ctx.send(f"```⌛ Du kannst noch nicht wieder arbeiten```")
                    return
                else:
                    data["economy"]["work"][str(ctx.author.id)] = False
            except:
                data["economy"]["work"][str(ctx.author.id)] = False

            work_money = random.randint(100, 500)
            money = data["economy"]["money"][str(ctx.author.id)]
            data["economy"]["money"][str(ctx.author.id)] = money + work_money

            professions = ["Informatiker", "Bauarbeiter", "Influencer", "Fotograf", "Designer", "Ingenieur", "Analytiker", "Doktor", "Zahnartzt"]
            profession = random.choice(professions)

            await ctx.send(f"```👞 Du hast als {profession} gearbeitet und {work_money}💵 verdient```")
            with open("", "w") as data_file:
                data = json.dump(data, data_file, indent=4)

            with open("", "r") as data_file:
                data = json.load(data_file)

            await asyncio.sleep(600)
            with open("", "r") as data_file:
                data = json.load(data_file)

            data["economy"]["work"][str(ctx.author.id)] = True

            with open("", "w") as data_file:
                data = json.dump(data, data_file, indent=4)
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Command {Fore.CYAN}work{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

def setup(client):
    client.add_cog(work(client))
