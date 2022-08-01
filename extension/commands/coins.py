import nextcord
from nextcord.ext import commands

import json

from colorama import Fore
import datetime

import requests

class coins(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def coins(self, ctx):
        try:
            stock_data = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd').json()
            with open("", "r") as data_file:
                data = json.load(data_file)

            own_stocks = {}
            for stock in data["economy"]["coins"]:
                if str(ctx.author.id) in data["economy"]["coins"][stock]: own_stocks[stock] = data["economy"]["coins"][stock][str(ctx.author.id)]

            if len(own_stocks) == 0:
                await ctx.send("```❌ Du hast keine Coins```")
                return

            msg = "    🚀 Deine Coins\n\n"
            all_price = 0
            for stock, quantity in own_stocks.items():
                for index in range(len(stock_data)):
                    if (stock_data[index]["symbol"] == stock) and (int(data["economy"]["coins"][stock][str(ctx.author.id)]) > 0):
                        price = int(stock_data[index]["current_price"]*quantity)
                        name = stock_data[index]["name"]
                        quantity = quantity
                        msg += f"💳 {quantity} {stock} ({name}) ≙ {price}💵\n"
                        all_price += price

            msg += f"\n📜 Total : {all_price}💵"
            await ctx.send(f"```{msg}```")
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Command {Fore.CYAN}coins{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

def setup(client):
    client.add_cog(coins(client))
