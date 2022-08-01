import nextcord
from nextcord.ext import commands

from colorama import Fore
import datetime

class act(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def act(self, ctx, member : commands.MemberConverter, *, message : str):
        try:
            await ctx.message.delete()
            
            webhook = await ctx.channel.create_webhook(name=member.name)
            await webhook.send(message, username=member.name, avatar_url=member.avatar)

            await webhook.delete()
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Command {Fore.CYAN}act{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

def setup(client):
    client.add_cog(act(client))