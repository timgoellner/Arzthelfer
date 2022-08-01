import nextcord
from nextcord.ext import commands

import json

from colorama import Fore
import datetime

class mute(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def mute(self, ctx, member : commands.MemberConverter, *, reason = "Keine"):
        try:
            if not ctx.author.guild_permissions.kick_members:
                await ctx.channel.send("```🔐Du hast keine Berechtigungen für diesen Befehl```")
                return

            with open("", "r") as data_file:
                data = json.load(data_file)

            mute_role = ctx.guild.get_role(data["moderation"]["mute_role"])
            if mute_role in member.roles:
                await ctx.channel.send(f"```❌ {member} ist bereits gemuted```")
                return

            await member.add_roles(mute_role)
            await ctx.channel.send(f"```🔇 {member} wurde gemuted\n📃 Begründung: {reason}```")
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Command {Fore.CYAN}mute{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("```❌ Bitte gebe alle nötigen argumente an```")

def setup(client):
    client.add_cog(mute(client))
