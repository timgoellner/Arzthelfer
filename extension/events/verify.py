import nextcord
from nextcord.ext import commands

import json

from colorama import Fore
import datetime

import random
import asyncio

class verify(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        try:
            with open("", "r") as data_file:
                data = json.load(data_file)

            global role, channel, verify_msg
            guild = self.client.get_guild(data["verify"]["guild"])
            role = guild.get_role(data["verify"]["verify_role"])
            channel = self.client.get_channel(data["verify"]["verify_channel"])

            await channel.purge(limit=10)

            verify_msg = await channel.send(embed=gen_embed())
            await verify_msg.add_reaction('✅')

            while str(self.client.status) == 'online':
                await asyncio.sleep(3)
                await verify_msg.edit(embed=gen_embed())

        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Event {Fore.CYAN}verify{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if user == self.client.user: return
        if reaction.message.channel == channel and reaction.emoji == '✅':
            await user.add_roles(role)
            await reaction.message.remove_reaction('✅', user)

def setup(client):
    client.add_cog(verify(client))

def gen_embed():
    embed = nextcord.Embed(color=nextcord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), title="Discord Verify", description="Wenn du dir die **Server Regeln** in <#775400745570271272> durchgelesen hast, musst du nur auf das :white_check_mark: **Emoji** reagieren um viel mehr auf diesem Discord machen zu können, **Viel Spaß!**\nReagiere einfach auf die Nachricht um die **Eingewisen Rolle** zu beckommen")
    return embed
