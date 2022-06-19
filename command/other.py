import discord
from config import PREFIX
from discord.ext import commands
from render import render

client = commands.Bot(command_prefix=PREFIX)

class other:
    async def commands(ctx):
        await ctx.send(f'{PREFIX}help')

    async def eval(ctx):
        try:
            await render.DrawEmbSuccessfully(ctx, eval(ctx.message.content[6:]))
        except:
            await render.DrawEmbError(ctx, 'Eval error.')
