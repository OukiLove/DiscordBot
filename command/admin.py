from unittest import expectedFailure
import discord
import asyncio
from discord.ext import commands
from config import PREFIX, EMB_COLOR
from render import render

class admin:
    async def ban(ctx, member: discord.Member, reason):
        try:
            await member.ban(reason=reason)
            await render.DrawEmbSuccessfully(ctx, 'User {} was baned!'.format(member.mention))
        except:
            await render.DrawEmbError(ctx, '$ban member reason')

    async def kick(ctx, member: discord.Member, *, reason):
        try:
            await member.kick( reason = reason)
            await render.DrawEmbSuccessfully(ctx, 'User {} was kicked!'.format(member.mention))
        except:
            await render.DrawEmbError(ctx, '$kick member reason')

    async def mute(ctx, member: discord.Member, time: int, reason):
        try:
            muterole = discord.utils.get(ctx.guild.roles, id = 988037054808084490)
            await render.DrawEmbSuccessfully(ctx, 'User {} was muted!'.format(member.mention))
            await member.add_roles(muterole)
            await asyncio.sleep(time * 60)
            await member.remove_roles(muterole)
        except:
            await render.DrawEmbError(ctx, '$mute member time reason')

    async def unmute(ctx, member: discord.Member):
        try:
            muterole = discord.utils.get(ctx.guild.roles, id = 988037054808084490)
            await member.remove_roles(muterole)
            await render.DrawEmbSuccessfully(ctx, 'User {} was unmuted!'.format(member.mention))
        except:
            await render.DrawEmbError(ctx, '$unmute member')

    async def info(ctx,member:discord.Member):
        emb = discord.Embed(title=':white_check_mark: User information', color=EMB_COLOR)
        await ctx.channel.purge(limit=0)
        emb.add_field(name='Server invite date:', value=member.joined_at, inline=False)
        emb.add_field(name='Nickname:', value=member.display_name, inline=False)
        emb.add_field(name= 'ID:', value=member.id, inline=False)
        emb.add_field(name= 'Account created:', value=member.created_at.strftime('%a,%#d %B %Y, %I:%M %p UTC'), inline=False)
        emb.set_thumbnail(url=member.avatar_url)
        emb.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        await ctx.author.send(embed = emb)
        await ctx.send('***Detailed information about the user was sent in private messages.***')

    async def clear(ctx, amout):
        try:
            await ctx.channel.purge(limit=int(amout))
            await render.DrawEmbSuccessfully(ctx, 'Chanel cleared!')
        except:
            await render.DrawEmbError(ctx, '$clear amout')