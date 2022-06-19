import discord
from discord.ext import commands
from config import OWNER, TOKEN, PREFIX
from command.music import music
from command.admin import admin
from command.other import other
from render import render

client = commands.Bot(command_prefix=PREFIX)

class Music:
    @client.command()
    async def play(ctx, url):
        await music.play(ctx, url)

    @client.command()
    async def pause(ctx):
        await music.pause(ctx)

    @client.command()
    async def stop(ctx):
        await music.stop(ctx)

    @client.command()
    async def resume(ctx):
        await music.resume(ctx)

    @client.command()
    async def leave(ctx):
        await music.leave(ctx)

class Admin:
    @client.command()
    async def ban(ctx, member: discord.Member, reason):
        if ctx.author.guild_permissions.administrator:
            await admin.ban(ctx, member, reason)
        else:
            await render.DrawEmbError(ctx, "You don't have the permission to use this command.")

    @client.command()
    async def kick(ctx, member: discord.Member, *, reason):
        if ctx.author.guild_permissions.administrator:
            await admin.kick(ctx, member, reason)
        else:
            await render.DrawEmbError(ctx, "You don't have the permission to use this command.")

    @client.command()
    async def mute(ctx, member: discord.Member, time: int, reason):
        if ctx.author.guild_permissions.administrator:
            await admin.mute(ctx, member, time, reason)
        else:
            await render.DrawEmbError(ctx, "You don't have the permission to use this command.")
    
    @client.command()
    async def unmute(ctx, member: discord.Member):
        if ctx.author.guild_permissions.administrator:
            await admin.unmute(ctx, member)
        else:
            await render.DrawEmbError(ctx, "You don't have the permission to use this command.")

    @client.command()
    async def info(ctx, member:discord.Member):
        if ctx.author.guild_permissions.administrator:
            await admin.info(ctx, member)
        else:
            await render.DrawEmbError(ctx, "You don't have the permission to use this command.")

    @client.command()
    async def clear(ctx, amout):
        if ctx.author.guild_permissions.administrator:
            await admin.clear(ctx, amout)
        else:
            await render.DrawEmbError(ctx, "You don't have the permission to use this command.")

class Other:
    @client.command()
    async def commands(ctx):
        await other.commands(ctx)

    @client.command()
    async def eval(ctx):
        await other.eval(ctx)

client.run(TOKEN)