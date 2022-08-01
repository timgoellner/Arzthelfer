import nextcord
from nextcord.ext import commands

from colorama import Fore
import datetime

import requests

class stocks(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def stocks(self, ctx, count : int = None):
        try:
            if (count == None) or (count > 75) or (count < 1):
                await ctx.send("```❌ Bitte gebe an wie viele Währungen dir angezeigt werden sollen (1 bis 75)```")
                return

            stock_data = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd').json()
            msg = "   🚀 Alle Möglichen Kryptowährungen\n\n"

            for index in range(count):
                name = stock_data[index]["name"]
                symbole = stock_data[index]["symbol"]
                msg += f"🏷️ {symbole} >> ({name})\n"

            await ctx.send(f"```{msg}```")
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Command {Fore.CYAN}stocks{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

def setup(client):
    client.add_cog(stocks(client))