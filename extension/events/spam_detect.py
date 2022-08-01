import nextcord
from nextcord.ext import commands

import json

from colorama import Fore
import datetime

import asyncio

class spam_detect(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, msg):
        try:
            with open("", "r+") as spam_file:
                cnt = 0
                for line in spam_file:
                    if line.strip('\n') == str(msg.author.id):
                        cnt += 1

                if cnt >= 4:
                    with open("", "r") as data_file:
                        data = json.load(data_file)

                    mute_role = msg.guild.get_role(data["moderation"]["mute_role"])
                    await msg.author.add_roles(mute_role)

                    await asyncio.sleep(600)

                    await msg.author.remove_roles(mute_role)
                else:
                    if not msg.author.bot:
                        spam_file.writelines(f"{str(msg.author.id)}\n")
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Event {Fore.CYAN}spam_detect{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

def setup(client):
    client.add_cog(spam_detect(client))
