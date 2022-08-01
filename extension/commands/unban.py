import nextcord
from nextcord.ext import commands

from colorama import Fore
import datetime

class unban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def unban(self, ctx, member):
        try:
            if not ctx.author.guild_permissions.ban_members:
                await ctx.channel.send("```🔐Du hast keine Berechtigungen für diesen Befehl```")
                return

            banned_users = await ctx.guild.bans()
            member_name, member_hash = member.split("#")

            for unban_user in banned_users:
                user = unban_user.user
                if (user.name, user.discriminator) == (member_name, member_hash):
                    await ctx.guild.unban(user)
                    await ctx.channel.send(f"```🔓 {member} wurde von dem Server unbannt```")
                    return
            await ctx.send(f"```🕵️ Der Benutzer {member} konnte nicht gefunden werden```")
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Command {Fore.CYAN}unban{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("```❌ Bitte gebe alle nötigen argumente an```")

def setup(client):
    client.add_cog(unban(client))