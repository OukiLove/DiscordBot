import discord
from youtube_dl import YoutubeDL
from render import render

class music:
    async def play(ctx, url):
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with YoutubeDL(ydl_opts) as ydl:
            try:
                if not ctx.voice_client:
                    await ctx.message.author.voice.channel.connect()
                info_dict = ydl.extract_info(url, download=False)
                song_title = info_dict.get('title', None)
                song_url = info_dict.get('url', None)
                if song_title is None:
                    await render.DrawEmbError(ctx, 'Could not find the song.')
                else:
                    await render.DrawEmbSuccessfully(ctx, f'Playing {song_title}')
                    ctx.voice_client.play(discord.FFmpegPCMAudio(song_url))
            except:
                await render.DrawEmbError(ctx, 'Could not play the song.')

    async def pause(ctx):
        try:
            ctx.voice_client.pause()
            await render.DrawEmbSuccessfully(ctx, 'Paused the song.')
        except:
            await render.DrawEmbError(ctx, 'Could not pause the song.')
    
    async def resume(ctx):
        try:
            ctx.voice_client.resume()
            await render.DrawEmbSuccessfully(ctx, 'Resumed the song.')
        except:
            await render.DrawEmbError(ctx, 'Could not resume the song.')

    async def stop(ctx):
        try:
            ctx.voice_client.stop()
            await render.DrawEmbSuccessfully(ctx, 'Stopped the song.')
        except:
            await render.DrawEmbError(ctx, 'Could not stop the song.')

    async def leave(ctx):
        try:
            await ctx.voice_client.disconnect()
            await render.DrawEmbSuccessfully(ctx, 'Left the voice channel.')
        except:
            await render.DrawEmbError(ctx, 'Could not leave the voice channel.')