import nextcord
from nextcord.ext import commands

import json

from colorama import Fore
import datetime

with open('data.json', "r") as data_file:
    data = json.load(data_file)

token = data["env"]["token"]
prefix = data["env"]["prefix"]
extensions = data["env"]["cogs"]

client = commands.Bot(command_prefix=prefix)
client.remove_command('help')

@client.command()
async def extension(ctx, cmd : str, extension="-"):
    if not ctx.author.guild_permissions.administrator:
        await ctx.send(f"```❌ Du hast keine Rechte für diesen Command```")
        return

    if (not extension in data["env"]["cogs"]) and cmd != "list":
        await ctx.send(f"```❌ {extension} ist keine extension```")
        return

    if cmd.startswith("load"):
        client.load_extension(extension)
        msg = f"✔️ Extension {extension} wurde geladen"
        print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.GREEN}LOADED{Fore.RESET}] Cog {Fore.CYAN}{extension}{Fore.RESET} wurde geladen{Fore.LIGHTBLACK_EX}")
    elif cmd.startswith("unload"):
        client.unload_extension(extension)
        msg = f"✔️ Extension {extension} wurde unloaded"
        print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.LIGHTRED_EX}UNLOADED{Fore.RESET}] Cog {Fore.CYAN}{extension}{Fore.RESET} wurde unloaded{Fore.LIGHTBLACK_EX}")
    elif cmd.startswith("list"):
        extensions = ""

        for extension in data["env"]["cogs"]:
            if extension in client.extensions:
                extensions += f" ✔️ {extension}\n"
            else:
                extensions += f" ❌ {extension}\n"

        await ctx.send(f"```   💽 Alle Extensions\n{extensions}```")
        return
    else:
        msg = f"❌ {cmd} ist keine gültiger command"

    await ctx.send(f"```{msg}```")

if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension(extension)
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.GREEN}LOADED{Fore.RESET}] Cog {Fore.CYAN}{extension}{Fore.RESET} wurde geladen{Fore.LIGHTBLACK_EX}")
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Cog {Fore.CYAN}{extension}{Fore.RESET} konnte nicht geladen werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

client.run(token)