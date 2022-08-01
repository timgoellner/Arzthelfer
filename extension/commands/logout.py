import nextcord
from nextcord.ext import commands

from colorama import Fore
import datetime

class logout(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def logout(self, ctx):
        try:
            if not ctx.author.id in [695231432989343836,523239444053098499]:
                await ctx.channel.send("```🔐Du hast keine Berechtigungen für diesen Befehl```")
                return

            await ctx.send("```🛑 Logging out...```")
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.MAGENTA}LOGGOUT{Fore.RESET}] Bot logged out...{Fore.LIGHTBLACK_EX}")
            await self.client.close()
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Command {Fore.CYAN}logout{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

def setup(client):
    client.add_cog(logout(client))
