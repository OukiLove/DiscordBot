import discord
from discord.ext import commands
from config import OWNER, TOKEN, PREFIX
from command.music import music
from command.admin import admin
from command.other import other
from render import render

client = commands.Bot(command_prefix=PREFIX, help_command=None)

class Music:
    @client.command()
    async def play(ctx, url):
        try:
            await music.play(ctx, url)
        except:
            await render.DrawEmbError(ctx, 'play <url>')

    @client.command()
    async def pause(ctx):
        try:
            await music.pause(ctx)
        except:
            await render.DrawEmbError(ctx, 'Could not pause the song.')

    @client.command()
    async def stop(ctx):
        try:
            await music.stop(ctx)
        except:
            await render.DrawEmbError(ctx, 'Could not stop the song.')

    @client.command()
    async def resume(ctx):
        try:
            await music.resume(ctx)
        except:
            await render.DrawEmbError(ctx, 'Could not resume the song.')

    @client.command()
    async def leave(ctx):
        try:
            await music.leave(ctx)
        except:
            await render.DrawEmbError(ctx, 'Could not leave the voice channel.')

class Admin:
    @client.command()
    async def ban(ctx, member: discord.Member, reason):
        if ctx.author.id == OWNER:
            try:
                await admin.ban(ctx, member, reason)
            except:
                await render.DrawEmbError(ctx, 'ban <member> <reason>')
        else:
            await render.DrawEmbError(ctx, 'You dont have the permission to use this command.')

    @client.command()
    async def kick(ctx, member: discord.Member, *, reason):
        if ctx.author.id == OWNER:
            try:
                await admin.kick(ctx, member, reason)
            except:
                await render.DrawEmbError(ctx, 'kick <member> <reason>')
        else:
            await render.DrawEmbError(ctx, 'You dont have the permission to use this command.')

    @client.command()
    async def mute(ctx, member: discord.Member, time: int, reason):
        if ctx.author.id == OWNER:
            try:
                await admin.mute(ctx, member, time, reason)
            except:
                await render.DrawEmbError(ctx, 'mute <member> <time> <reason>')
        else:
            await render.DrawEmbError(ctx, 'You dont have the permission to use this command.')
    
    @client.command()
    async def unmute(ctx, member: discord.Member):
        if ctx.author.id == OWNER:
            try:
                await admin.unmute(ctx, member)
            except:
                await render.DrawEmbError(ctx, 'unmute <member>')
        else:
            await render.DrawEmbError(ctx, 'You dont have the permission to use this command.')

    @client.command()
    async def info(ctx, member:discord.Member):
        if ctx.author.id == OWNER:
            try:
                await admin.info(ctx, member)
            except:
                await render.DrawEmbError(ctx, 'info <member>')
        else:
            await render.DrawEmbError(ctx, 'You dont have the permission to use this command.')

    @client.command()
    async def clear(ctx, amout):
        if ctx.author.id == OWNER:
            try:
                await admin.clear(ctx, amout)
            except:
                await render.DrawEmbError(ctx, 'clear <amout>')
        else:
            await render.DrawEmbError(ctx, 'You dont have the permission to use this command.')

class Other:
    @client.command()
    async def help(ctx):
        try:
            await other.help(ctx)
        except:
            await render.DrawEmbError(ctx, 'Error.')

    @client.command()
    async def eval(ctx):
        try:
            await other.eval(ctx)
        except:
            await render.DrawEmbError(ctx, 'Eval error.')

    @client.command()
    async def exec(ctx):
        try:
            await other.exec(ctx)
        except:
            await render.DrawEmbError(ctx, 'Exec error.')

    @client.command()
    async def addbot(ctx):
        try:
            await other.addbot(ctx)
        except:
            await render.DrawEmbError(ctx, 'Error.')

    @client.command()
    async def status(ctx):
        try:
            await other.status(ctx)
        except:
            await render.DrawEmbError(ctx, 'Error.')

@client.event()
async def on_ready():
    activity = discord.Game(name="{}help".format(PREFIX), type=3)
    await client.change_presence(status=discord.Status.idle, activity=activity)
    
client.run(TOKEN)