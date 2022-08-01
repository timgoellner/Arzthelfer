import nextcord
from nextcord.ext import commands

from colorama import Fore
import datetime

import requests

class stock(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def stock(self, ctx, stock : str = None):
        try:
            if stock == None:
                await ctx.send("```❌ Bitte gebe eine Währunge die dir angezeigt werden soll an```")
                return

            stock_data = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd').json()
            msg = f"   🚀 Information zur Kryptowährunge {stock}\n\n"

            found = False
            for index in range(len(stock_data)):
                if stock_data[index]["symbol"] == stock.lower():
                    name = stock_data[index]["name"]
                    price = round(stock_data[index]["current_price"], 2)
                    change = round(stock_data[index]["price_change_24h"], 2)
                    change_percent = round(stock_data[index]["price_change_percentage_24h"], 2)
                    found = True

            if found == False:
                await ctx.send(f"```❌ Die Währung '{stock}' wurde nicht gefunden```")
                return

            if str(change).startswith('-'): ext_emoji = '📉'
            else: ext_emoji = '📈'

            await ctx.send(f"```   🚀 Information zur Kryptowährunge {stock} ({ext_emoji})\n\n🏷️ Name : {name}\n💰 Geld : {price}💵\n{ext_emoji} Change 24h : {change}💵\n🧮 Change Percent 24h : {change_percent}%```")
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Command {Fore.CYAN}stock{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

def setup(client):
    client.add_cog(stock(client))