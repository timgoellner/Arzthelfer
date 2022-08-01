import nextcord
from nextcord.ext import commands

from colorama import Fore
import datetime

class radio(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def radio(self, ctx, sender : str = None):
        try:
            channel = ctx.author.voice.channel
            voice_client = nextcord.utils.get(self.client.voice_clients, guild=ctx.guild)

            if channel == None:
                await ctx.send("```❌ Du bist in keinem Voice Channel```")
                return
            if voice_client == None: voice_client = await channel.connect()
            else:
                voice_client.pause()
                await voice_client.move_to(channel)

            if sender == None or sender.lower() == "1live": source = nextcord.FFmpegPCMAudio("https://f121.rndfnk.com/ard/wdr/1live/live/mp3/128/stream.mp3?sid=21uwKq380RpGMu5DUIdtiHAdI1t&token=u0znVR4apLhkpVki-6zfH94FMRVqHAfBeIK7sKc8QvQ&tvf=OfFMP2ZHvhZmMTIxLnJuZGZuay5jb20")
            elif sender.lower() == "wdr2": source = nextcord.FFmpegPCMAudio("https://d131.rndfnk.com/ard/wdr/wdr2/muensterland/mp3/128/stream.mp3?sid=2BlbJQHZXZlCBbVJzGM71HFH5qz&token=N51zsuItyzG9eMhkKPCtmcjJ1QAdNkg4PrRuzP3akTs&tvf=AiRTBCakABdkMTMxLnJuZGZuay5jb20")
            elif sender.lower() == "wdr5": source = nextcord.FFmpegPCMAudio("https://f141.rndfnk.com/ard/wdr/wdr5/live/mp3/128/stream.mp3?sid=2BnKYwhdvwrnZrewf2dUWgN52ZR&token=-IrzbcQlZOVTdwbScMyjGO-iGwjn00crA2Eu7vRWvSU&tvf=iv1S3kXUABdmMTQxLnJuZGZuay5jb20")
            elif sender.lower() == "iloveradio": source = nextcord.FFmpegPCMAudio("https://streams.ilovemusic.de/iloveradio1.mp3")
            elif sender.lower() == "schlagerparadies": source = nextcord.FFmpegPCMAudio("http://webstream.schlagerparadies.de/schlagerparadies128k.mp3")
            else:
                await ctx.send("```❌ Radio Sender nicht gültig```")
                await voice_client.disconnect()
                return
            voice_client.play(source)

            await ctx.send(f"```📡 Spiele Radio in '{channel.name}'```")
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Command {Fore.CYAN}radio{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

def setup(client):
    client.add_cog(radio(client))
