# -*- coding: utf-8 -*-
import random

import discord
from discord.ext import commands

from texts.ptbr import quemsoueu, saudacoes
from utils import find


class Greetings(commands.Cog):
	"""Mensagem de apresentação da Janet"""

	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_member_join(self, member):
		guild = member.guild
		channel = find.find_channel(guild, 'geral')
		if channel is not None:
			await channel.send(random.choice(saudacoes))
		else:
			await member.create_dm()
			await member.dm_channel.send(random.choice(saudacoes))

	@commands.command(name='ola', help='De olá para alguém')
	async def hello(self, ctx, member: discord.Member = None):
		member = member or ctx.author
		if member is None or ctx.author.id != member.id:
			await ctx.send(f'Olá  {member.name} Sou a Janet Prazer em te conhecer ')
		else:
			await ctx.send(f'Olá')

	@commands.command(name='apresentacao', help='Apresentação da Janet')
	async def apresentation(self, ctx):
		await ctx.send(quemsoueu)

	async def cog_command_error(self, ctx, error):
		if isinstance(error, commands.errors.BadArgument):
			await ctx.send(f'Tente dar olá para alguém que seja um Humano')


def setup(bot):
	bot.add_cog(Greetings(bot))
