import nextcord
from nextcord.ext import commands

from colorama import Fore
import datetime

import youtube_dl
import asyncio

class play(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def play(self, ctx, *, url):
        try:
            FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            YTDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}

            if ctx.author.voice == None:
                await ctx.send("```❌ Du bist nicht in einem Channel```")
                return

            global vc, vc_connect, voice_client
            vc = ctx.author.voice.channel
            vc_connect = ctx.voice_client
            if vc_connect is None:
                await vc.connect()

            voice_client = ctx.voice_client

            with youtube_dl.YoutubeDL(YTDL_OPTIONS) as ytdl:
                if url.startswith("https://"): info = ytdl.extract_info(url, download=False)
                else: info = ytdl.extract_info(f"ytsearch:{url}", download=False)['entries'][0]
                
                playlist.append(info)

                title = info["title"]
                try: artist = "von '"+info["artist"]+"'"
                except: artist = ""
                if (vc_connect == None or not voice_client.is_playing()) and not voice_client.is_paused(): await ctx.send(f"```📻 Spiele '{title}' {artist}```")
                else: await ctx.send(f"```➕ '{title}' {artist} wurde zur Playlist hinzugefügt```")
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Command {Fore.CYAN}play{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

    @commands.command()
    async def clear(self, ctx):
        try:
            if len(playlist) < 1:
                await ctx.send("```❌ Kein Lied in der Playlist```")
                return
            playlist.clear()
            await ctx.send("```✨ Playlist gecleart```")
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Command {Fore.CYAN}clear{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

    @commands.command()
    async def skip(self, ctx):
        try:
            if len(playlist) < 1:
                await ctx.send("```❌ Kein weiteres Lied in der Playlist```")
                return
            voice_client.stop()
            await ctx.send("```⏭️ Lied wird übersprungen```")
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Command {Fore.CYAN}skip{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

    @commands.command()
    async def stop(self, ctx):
        try:
            vc_connect = ctx.voice_client
            if (vc_connect is None) or (not vc_connect.is_playing()):
                await ctx.send("```❌ Ich spiele im Moment nichts```")
                return
            playlist.clear()   
            vc_connect.stop()
            await ctx.send(f"```🤐 Ich habe das aktuelle Lied gestoppt```")
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Command {Fore.CYAN}stop{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

    @commands.command()
    async def leave(self, ctx):
        try:
            vc_connect = ctx.voice_client
            if ctx.voice_client is None:
                await ctx.send("```❌ Ich bin nicht in einem Voice Channel```")
                return
            playlist.clear()   
            try: vc_connect.stop()
            except: pass
            await vc_connect.disconnect()
            await ctx.send(f"```👋 Ich bin {vc_connect.channel} geleavt```")
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Command {Fore.CYAN}leave{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

    @commands.command()
    async def playlist(self, ctx):
        try:
            if len(playlist) == 0:
                await ctx.send("```❌ Kein Lied in der Playlist```")
                return

            pl_msg = ""
            for song_idx, song in enumerate(playlist):
                title = song["title"]
                pl_msg += f"{song_idx+1} | {title}\n"

            await ctx.send(f"```   💿 Playlist\n\n{pl_msg}```")
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Command {Fore.CYAN}playlist{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

    @commands.Cog.listener()
    async def on_ready(self):
        try:
            FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            YTDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}

            while True:
                await asyncio.sleep(1)
                if len(playlist) > 0:
                    while voice_client.is_playing() or voice_client.is_paused():
                        await asyncio.sleep(1)
                    if len(playlist) > 0:
                        with youtube_dl.YoutubeDL(YTDL_OPTIONS) as ytdl:
                            info = playlist[0]
                            _url = info["formats"][0]["url"]
                            source = await nextcord.FFmpegOpusAudio.from_probe(_url, **FFMPEG_OPTIONS)

                            voice_client.play(source)
                            del playlist[0]

            print("-")
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Event {Fore.CYAN}player{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        try:
            channel = before.channel
            if channel == None: return
            if channel.guild.voice_client in self.client.voice_clients and len(channel.members) == 1:
                playlist.clear()   
                try: vc_connect.stop()
                except: pass
                await self.client.voice_clients[0].disconnect()
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Event {Fore.CYAN}voice_leave{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")

def setup(client):
    client.add_cog(play(client))
    global playlist
    playlist = []
