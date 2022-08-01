import nextcord
from nextcord.ext import commands

from colorama import Fore
import datetime

class ban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ban(self, ctx, member : commands.MemberConverter, *, reason = "Keine"):
        try:
            if not ctx.author.guild_permissions.ban_members:
                await ctx.channel.send("```🔐Du hast keine Berechtigungen für diesen Befehl```")
                return

            await member.ban(reason=reason)
            await ctx.channel.send(f"```🔨 {member} wurde von dem Server gebannt\n📃 Begründung: {reason}```")
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Command {Fore.CYAN}ban{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("```❌ Bitte gebe alle nötigen argumente an```")

def setup(client):
    client.add_cog(ban(client))