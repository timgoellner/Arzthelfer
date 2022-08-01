import nextcord
from nextcord.ext import commands

import json

from colorama import Fore
import datetime

class truncate(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def truncate(self, ctx, msgs = 1):
        try:
            if not ctx.author.guild_permissions.manage_messages:
                await ctx.send("```❌ Du hast keine Berechtigungen für diesen Befehl```")
                return

            if msgs < 1 or msgs > 20:
                await ctx.send("```❌ Du kannst nur 1 bis 20 Nachrichten löschen```")
                return

            await ctx.channel.purge(limit=msgs+1)

            await ctx.send(f"```🗑️ {msgs} Nachricht(-en) wurden gelöscht```", delete_after=3)
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Command {Fore.CYAN}truncate{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

def setup(client):
    client.add_cog(truncate(client))