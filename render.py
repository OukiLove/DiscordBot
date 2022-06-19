import discord
from config import EMB_COLOR

class render:
    async def DrawEmbError(ctx, text):
        emb = discord.Embed(color=EMB_COLOR)
        emb.add_field(name=':no_entry:', value=text)
        await ctx.send(embed = emb)

    async def DrawEmbSuccessfully(ctx, text):
        emb = discord.Embed(color=EMB_COLOR)
        emb.add_field(name=':white_check_mark:', value=text)
        await ctx.send(embed = emb)