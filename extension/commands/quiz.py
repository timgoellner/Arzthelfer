import nextcord
from nextcord.ext import commands

from colorama import Fore
import datetime

import json
import random

class quiz(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def quiz(self, ctx):
        try:
            with open("", "r") as data_file:
                data = json.load(data_file)

            global question, answers, question_name
            question = data[random.randint(0, len(data))-1]
            answers = question["answers"]
            random.shuffle(answers)
            question_name = question["question"]

            global quiz_msg
            quiz_msg = await ctx.send(f"```❓ Frage: {question_name}\n\nAntworten:\n  🇦) {answers[0]}\n  🇧) {answers[1]}\n  🇨) {answers[2]}\n  🇩) {answers[3]}\n\nReagiere mit dem richtigen Buchstaben```")

            for emoji in ['🇦','🇧','🇨','🇩']:
                await quiz_msg.add_reaction(emoji)

        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Command {Fore.CYAN}quiz{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

    @commands.command()
    async def quizes(self, ctx):
        with open("", "r") as data_file:
            data = json.load(data_file)

        try: quizes = data["quiz"]["quizes"][str(ctx.author.id)]
        except:
            await ctx.send("```❌ Du hast bisher keine Quizes gemacht```")
            return

        await ctx.send(f"```❔ Du hast {quizes} Quizes richtig beantwortet```")

    @commands.command()
    async def suggest_quiz(self, ctx, *, question : str):
        with open("", "r") as data_file:
            data = json.load(data_file)

        channel = ctx.guild.get_channel(data["quiz"]["suggest_channel"])
        await channel.send(f"```✋ Quiz Vorschlag von {ctx.author}\n❔ {question}```")
        await ctx.send("```✔️ Vorschlag wurde eingereicht```")

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if user == self.client.user or quiz_msg.id != reaction.message.id: return
        converter = {'🇦':0,'🇧':1,'🇨':2,'🇩':3}
        if answers[converter[reaction.emoji]] == question["correct"]: result = "richtig (🏆)"
        else: result = "falsch (🚫)"

        win_text = []
        for answer in answers:
            if answer == question["correct"] and result == "richtig (🏆)": win_text.append('✔️')
            elif answer == question["correct"] and result == "falsch (🚫)": win_text.append('❌')
            else: win_text.append('   ')

        if result == "richtig (🏆)": win_sum = 150
        else: win_sum = -50

        with open("", "r") as data_file:
            data = json.load(data_file)

        try: quizes = data["quiz"]["quizes"][str(user.id)]
        except: quizes = 0

        if result == "richtig (🏆)": data["quiz"]["quizes"][str(user.id)] = quizes + 1

        money = int(data["economy"]["money"][str(user.id)])
        data["economy"]["money"][str(user.id)] = (money + win_sum)

        with open("", "w") as data_file:
            data = json.dump(data, data_file, indent=4)

        await quiz_msg.clear_reactions()
        await quiz_msg.edit(f"```❓ Frage: {question_name}\n\nAntworten:\n{win_text[0]}🇦) {answers[0]}\n{win_text[1]}🇧) {answers[1]}\n{win_text[2]}🇨) {answers[2]}\n{win_text[3]}🇩) {answers[3]}\n\n🕹️ Ergebniss: {result}\n💰 Money : {win_sum}💵```")

def setup(client):
    client.add_cog(quiz(client))
