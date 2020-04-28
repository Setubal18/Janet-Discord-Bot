# -*- coding: utf-8 -*-
import random

import discord
from discord.ext import commands

from texts.ptbr import quemsoueu, saudacoes


class Greetings(commands.Cog):
	"""Mensagem de apresentação da Janet"""

	def __init__(self, bot):
		self.bot = bot
		self._lest_member = None

	@commands.Cog.listener()
	async def on_member_join(self, member):
		print('member', member)
		channel = member.guild.system_channel
		print('channel', channel)
		if channel is not None:
			await channel.send(random.choice(saudacoes))
		else:
			await channel.send(random.choice(saudacoes))

	@commands.command(name='ola', help='De olá para alguém')
	async def hello(self, ctx, *, member: discord.Member = None):
		member = member or ctx.author
		if self._lest_member is None or self._lest_member.id != member.id:
			await ctx.send(f'No Contex msg {member.name}')
		else:
			await ctx.send(f'Hello {member.name}  acho que já te vi em algum lugar')
		self._last_member = member

	@commands.command(name='apresentacao', help='Apresentação da Janet')
	async def apresentation(self, ctx):
		await ctx.send(quemsoueu)


def setup(bot):
	bot.add_cog(Greetings(bot))
