import nextcord
from nextcord.ext import commands

import json

from colorama import Fore
import datetime

class answer(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def answer(self, ctx, cmd : str, msg : str = None, answer : str = None):
        try:
            with open("", "r") as data_file:
                data = json.load(data_file)

            if cmd == "create":
                if (msg == None) or (answer == None):
                    await ctx.send("```❌ Bitte gebe alle Argumente an```")
                    return

                data["answer"][msg] = answer
                await ctx.send(f"```📖 Auto Antwort auf '{msg}' zu '{answer}' wurde erstellt```")
            elif cmd == "remove":
                if (msg == None):
                    await ctx.send("```❌ Bitte gebe alle Argumente an```")
                    return

                try:
                    data["answer"].pop(msg)
                    await ctx.send(f"```📕 Auto Antwort auf '{msg}' wurde gelöscht```")
                except:
                    await ctx.send(f"```❌ Die Auto Antwort auf '{msg}' existiert nicht```")
                    return
            elif cmd == "list":
                msg = "   📋 Alle Auto Antworten\n\n"
                cnt = 0
                for answer in data["answer"]:
                    cnt += 1
                    answer_msg = data["answer"][answer]
                    msg += f" 💬 '{answer}' >> '{answer_msg}'\n"
                if cnt == 0:
                    await ctx.send("```❌ Keine Auto Antworten vorhanden```")
                    return
                await ctx.send(f"```{msg}```")
            else:
                await ctx.send(f"```❌ Der Auto Antworten Command {cmd} existiert nicht```")

            with open("", "w") as data_file:
                data = json.dump(data, data_file, indent=4)

        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Command {Fore.CYAN}answer{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

def setup(client):
    client.add_cog(answer(client))
