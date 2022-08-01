import nextcord
from nextcord.ext import commands

from colorama import Fore
import datetime

class kick(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def kick(self, ctx, member : commands.MemberConverter, *, reason = "Keine"):
        try:
            if not ctx.author.guild_permissions.kick_members:
                await ctx.channel.send("```🔐Du hast keine Berechtigungen für diesen Befehl```")
                return

            await member.kick(reason=reason)
            await ctx.channel.send(f"```🔨 {member} wurde von dem Server gekickt\n📃 Begründung: {reason}```")
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Command {Fore.CYAN}kick{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("```❌ Bitte gebe alle nötigen argumente an```")

def setup(client):
    client.add_cog(kick(client))