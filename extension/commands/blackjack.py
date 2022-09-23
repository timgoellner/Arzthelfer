import nextcord
from nextcord.ext import commands

import json
import random

from colorama import Fore
import datetime

class blackjack(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def blackjack(self, ctx, bid: str):
        try:
            with open("D:\Programmieren\Python\Discord Bots\Eigene Projekte\SelbsthilfeMC\data.json", "r") as data_file:
                data = json.load(data_file)

            if ctx.channel.id != data["economy"]["blackjack"]["channel"]:
                bj_channel = ctx.guild.get_channel(data["economy"]["blackjack"]["channel"])
                await ctx.send(f"```❌ Dieser Befehl kann nur in #{bj_channel.name} ausgeführt werden```")
                return

            with open("D:\Programmieren\Python\Discord Bots\Eigene Projekte\SelbsthilfeMC\games.json", "r") as data_file:
                games_data = json.load(data_file)

            for game in games_data["blackjack"]:
                if int(games_data["blackjack"][game]["player"]) == ctx.author.id:
                    bj_msg = await ctx.channel.fetch_message(int(game))
                    await bj_msg.reply("```❌ Du musst das Spiel erst zuende spielen bevor du ein neues starten kannst```")
                    return

            if (bid.startswith('-') or (not bid.isdigit())) and bid != "all":
                await ctx.send(f"```❌ Du kannst nicht {bid} einsetzen, nur 1 bis ... 💵```")
                return
            elif bid == "all": bid = data["economy"]["money"][str(ctx.author.id)]

            bid = int(bid)

            if bid < 1:
                await ctx.send("```❌ Du musst mindestens 1💵 einsetzen```")
                return

            if bid > int(data["economy"]["money"][str(ctx.author.id)]):
                await ctx.send("```❌ Du hast nicht genug geld```")
                return

            cards = data["economy"]["blackjack"]["cards"]
            player_cards = [random.choice(cards), random.choice(cards)]
            while player_cards[0] == player_cards[1]: player_cards = [random.choice(cards), random.choice(cards)]
            dealer_cards = [random.choice(cards), data["economy"]["blackjack"]["unknown_card"]]

            player_value = player_cards[0]["value"] + player_cards[1]["value"]
            dealer_value = dealer_cards[0]["value"]

            bj_embed = nextcord.Embed(color = nextcord.Color.from_rgb(47, 49, 54), description=f"    - 🃏 Blackjack Spiel von {ctx.author} -")
            bj_embed.add_field(name="Player Cards", value=player_cards[0]["id"] + " " + player_cards[1]["id"] + f"\n\nValue: {player_value}")
            bj_embed.add_field(name="Dealer Cards", value=dealer_cards[0]["id"] + " " + dealer_cards[1]["id"] + f"\n\nValue: {dealer_value}")

            bj_msg = await ctx.send(embed=bj_embed)

            game_info = {
                "player": f"{ctx.author.id}",
                "bid": bid,
                "player_cards": player_cards,
                "dealer_cards": dealer_cards
            }

            games_data["blackjack"][str(bj_msg.id)] = game_info

            with open("D:\Programmieren\Python\Discord Bots\Eigene Projekte\SelbsthilfeMC\games.json", "w") as data_file:
                games_data = json.dump(games_data, data_file, indent=4)

            if player_value == 21: await bj_msg.add_reaction("❕")
            else:
                await bj_msg.add_reaction("🃏")
                await bj_msg.add_reaction("🛑")

        except Exception as error:
            print(error.with_traceback(tb))
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Command {Fore.CYAN}blackjack{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

def setup(client):
    client.add_cog(blackjack(client))