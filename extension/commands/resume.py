import nextcord
from nextcord.ext import commands

from colorama import Fore
import datetime

class resume(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def resume(self, ctx):
        try:
            vc = ctx.author.voice.channel
            vc_connect = ctx.voice_client
            if (vc_connect is None) or (not vc_connect.is_paused()):
                await ctx.send("```❌ Ich bin nicht gestoppt```")
                return

            ctx.voice_client.resume()
            await ctx.send("```▶️ Lied Resumed```")
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Command {Fore.CYAN}resume{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

def setup(client):
    client.add_cog(resume(client))