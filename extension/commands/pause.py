import nextcord
from nextcord.ext import commands

from colorama import Fore
import datetime

class pause(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def pause(self, ctx):
        try:
            vc = ctx.author.voice.channel
            vc_connect = ctx.voice_client
            if (vc_connect is None) or (vc_connect.is_paused()) or ((vc_connect.is_connected()) and (not vc_connect.is_playing())):
                await ctx.send("```❌ Ich Spiele nichts```")
                return

            ctx.voice_client.pause()
            await ctx.send("```⏸️ Lied Pausiert```")
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Command {Fore.CYAN}pause{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

def setup(client):
    client.add_cog(pause(client))