import nextcord
from nextcord.ext import commands

import json

from colorama import Fore
import datetime

class bad_word(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def bad_word(self, ctx, cmd : str, bad_word : str = None):
        try:
            if not ctx.author.guild_permissions.administrator:
                await ctx.channel.send("```🔐Du hast keine Berechtigungen für diesen Befehl```")
                return
                
            with open("", "r") as data_file:
                data = json.load(data_file)

            if cmd == "add":
                data["bad_words"].append(bad_word)
                await ctx.send(f"```📖 Bad Word '{bad_word}' wurde eingetragen```")
            elif cmd == "remove":
                try:
                    data["bad_words"].remove(bad_word)
                    await ctx.send(f"```📕 Bad Word '{bad_word}' wurde ausgetragen```")
                except:
                    await ctx.send(f"```❌ Die Bad Word '{bad_word}' ist nicht eingetragen```")
                    return
            elif cmd == "list":
                msg = "   📋 Alle Bad Words\n\n"
                cnt = 0
                for bad_word in data["bad_words"]:
                    cnt += 1
                    msg += f" 💬 '{bad_word}'\n"
                if cnt == 0:
                    await ctx.send("```❌ Keine Bad Words vorhanden```")
                    return
                await ctx.send(f"```{msg}```")
            else:
                await ctx.send(f"```❌ Der Bad Words Command {cmd} existiert nicht```")

            with open("", "w") as data_file:
                data = json.dump(data, data_file, indent=4)

        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Command {Fore.CYAN}bad_word{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

def setup(client):
    client.add_cog(bad_word(client))
