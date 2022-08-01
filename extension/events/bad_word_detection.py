import nextcord
from nextcord.ext import commands

import json

from colorama import Fore
import datetime

import asyncio

class bad_word_detection(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, msg):
        try:
            with open("", "r") as data_file:
                data = json.load(data_file)

            contents = str(msg.content).split(" ")

            for content in contents:
                if (data["bad_words"].count(content) > 0) and (not msg.author.bot):
                    await msg.delete()

                    role = msg.guild.get_role(data["moderation"]["mute_role"])
                    await msg.author.add_roles(role)

                    await asyncio.sleep(600)
                    await msg.author.remove_roles(role)
                    break
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Event {Fore.CYAN}bad_word_detection{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

def setup(client):
    client.add_cog(bad_word_detection(client))
