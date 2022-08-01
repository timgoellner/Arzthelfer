import nextcord
from nextcord.ext import commands

from colorama import Fore
import datetime

class join(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self, ctx):
        try:
            if ctx.author.voice is None:
                await ctx.send("```❌ Du bist nicht in einem Voice Channel```")
                return
            vc = ctx.author.voice.channel
            vc_connect = ctx.voice_client
            if vc_connect is None:
                await vc.connect()
            else:
                await vc_connect.disconnect()
                await vc.connect()
            await ctx.send(f"```🙌 Ich bin {vc} gejoint```")
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Command {Fore.CYAN}join{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

def setup(client):
    client.add_cog(join(client))