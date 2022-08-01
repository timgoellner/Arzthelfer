import nextcord
from nextcord.ext import commands

import json

from colorama import Fore
import datetime

import requests

class invest(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def invest(self, ctx, stock : str = None, count : int = 1):
        try:
            if stock == None:
                await ctx.send("```❌ Bitte gebe eine Währunge an```")
                return

            stock_data = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd').json()
            with open("", "r") as data_file:
                data = json.load(data_file)

            found = False
            for index in range(len(stock_data)):
                if stock_data[index]["symbol"] == stock.lower():
                    name = stock_data[index]["name"]
                    price = round(stock_data[index]["current_price"], 2)
                    found = True

            if found == False:
                await ctx.send(f"```❌ Die Währung '{stock}' wurde nicht gefunden```")
                return

            try: money = data["economy"]["money"][str(ctx.author.id)]
            except: money = 0

            try: coins = data["economy"]["coins"][stock.lower()][str(ctx.author.id)]
            except:
                try: data["economy"]["coins"][stock.lower()][str(ctx.author.id)] = 0
                except: data["economy"]["coins"][stock.lower()] = {str(ctx.author.id):0}
                with open("", "w") as data_file:
                    data = json.dump(data, data_file, indent=4)
                data_file.close()
                with open("", "r") as data_file:
                    data = json.load(data_file)
                coins = 0

            stock_money = int(price * count)
            if stock_money > money:
                await ctx.send(f"```❌ Du hast nicht genug Geld um {count} '{stock.lower()}' für {stock_money}💵 zu kaufen```")
                return
            elif stock_money == 0:
                await ctx.send(f"```❌ Du kannst keine coins für 0💵 kaufen```")
                return

            data["economy"]["money"][str(ctx.author.id)] = money-stock_money
            data["economy"]["coins"][stock.lower()][str(ctx.author.id)] = coins+count

            with open("", "w") as data_file:
                data = json.dump(data, data_file, indent=4)

            await ctx.send(f"```🚀 Du hast {count} '{stock.lower()}' für {stock_money}💵 gekauft```")
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Command {Fore.CYAN}invest{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

def setup(client):
    client.add_cog(invest(client))
