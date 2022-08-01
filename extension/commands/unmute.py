import nextcord
from nextcord.ext import commands

import json

from colorama import Fore
import datetime

class unmute(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def unmute(self, ctx, member : commands.MemberConverter):
        try:
            if not ctx.author.guild_permissions.kick_members:
                await ctx.channel.send("```🔐Du hast keine Berechtigungen für diesen Befehl```")
                return

            with open("", "r") as data_file:
                data = json.load(data_file)

            unmute_role = ctx.guild.get_role(data["moderation"]["mute_role"])
            if unmute_role not in member.roles:
                await ctx.channel.send(f"```❌ {member} ist nicht gemuted```")
                return

            await member.remove_roles(unmute_role)
            await ctx.channel.send(f"```🔉 {member} wurde unmuted```")
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Command {Fore.CYAN}unmute{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("```❌ Bitte gebe alle nötigen argumente an```")

def setup(client):
    client.add_cog(unmute(client))
