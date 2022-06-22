import discord
import sys
from config import PREFIX
from discord.ext import commands
from render import render

client = commands.Bot(command_prefix=PREFIX)

class other:
    async def help(ctx):
        await render.DrawEmbSuccessfully(ctx,f'''
Music: 
    {PREFIX}play <url>
    {PREFIX}stop
    {PREFIX}pause
    {PREFIX}resume
    {PREFIX}leave
Admin:
    {PREFIX}ban <member> <reason>
    {PREFIX}kick <member> <reason>
    {PREFIX}mute <member> <time> <reason>
    {PREFIX}unmute <member>
    {PREFIX}info <member>
    {PREFIX}clear <amout>
Other:
    {PREFIX}eval <code>
    {PREFIX}exec <code>
    {PREFIX}addbot
    {PREFIX}status
    {PREFIX}help
''')

    async def eval(ctx):
        try:
            await render.DrawEmbSuccessfully(ctx, eval(ctx.message.content[6:]))
        except:
            await render.DrawEmbError(ctx, 'Eval error.')

    async def exec(ctx):
        try:
            await render.DrawEmbSuccessfully(ctx, exec(ctx.message.content[6:]))
        except:
            await render.DrawEmbError(ctx, 'Exec error.')

    async def addbot(ctx):
        try:
            await render.DrawEmbSuccessfully(ctx, 'https://discord.com/api/oauth2/authorize?client_id=973494234256658452&permissions=8&scope=bot')
        except:
            await render.DrawEmbError(ctx, 'Error.')

    async def status(ctx):
        try:
            await render.DrawEmbSuccessfully(ctx, 'Bot is work.')
        except:
            await render.DrawEmbSuccessfully(ctx, 'Error.')