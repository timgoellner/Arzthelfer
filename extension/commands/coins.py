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
    async def coins(self, ctx, member : commands.MemberConverter() = None):
        try:
            stock_data = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd').json()
            with open("D:\Programmieren\Python\Discord Bots\Eigene Projekte\SelbsthilfeMC\data.json", "r") as data_file:
                data = json.load(data_file)

            if member == None: member = ctx.author

            own_stocks = {}
            for stock in data["economy"]["coins"]:
                if str(member.id) in data["economy"]["coins"][stock]: own_stocks[stock] = data["economy"]["coins"][stock][str(member.id)]

            if len(own_stocks) == 0:
                await ctx.send("```❌ Du hast keine Coins```")
                return

            msg = f"    🚀 Coins von {member}\n\n"
            all_price = 0
            coin_list = [[], []]
            max_len = [0, 0]

            for stock, quantity in own_stocks.items():
                for index in range(len(stock_data)):
                    if (stock_data[index]["symbol"] == stock) and (int(data["economy"]["coins"][stock][str(member.id)]) > 0):
                        coin_list.append({str(quantity)+" "+stock:int(stock_data[index]["current_price"]*quantity)})
                        all_price += int(stock_data[index]["current_price"]*quantity)
                        name = stock_data[index]["name"]
                        price = int(stock_data[index]["current_price"]*quantity)
                        coin_list[0].append(f"💳 {quantity} {stock} ({name})")
                        coin_list[1].append(f"{price}💵")

            for item in coin_list[0]:
                if len(item) > max_len[0]: max_len[0] = len(item)
            for price in coin_list[1]:
                if len(str(price)) > max_len[1]: max_len[1] = len(str(price))

            for idx, item in enumerate(coin_list[0]):
                spaces = 3
                spaces += max_len[0]-len(item)
                spaces += max_len[1]-len(str(coin_list[1][idx]))
                spaces_word = ""
                for _ in range(spaces): spaces_word += " "
                msg += f"{item}{spaces_word}{coin_list[1][idx]}\n"

            spaces = 3
            spaces += max_len[0]-len("📜 Total : ")
            spaces += max_len[1]-(len(str(all_price))+1)
            spaces_word = ""
            for _ in range(spaces): spaces_word += " "

            await ctx.send(f"```{msg}\n📜 Total : {spaces_word}{all_price}💵```")

        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Command {Fore.CYAN}coins{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

def setup(client):
    client.add_cog(coins(client))
