# -*- coding: utf-8 -*-

import re

from discord.ext import commands

from texts.ptbr import seuConvite


class Invite(commands.Cog):
	"""The description for Invite goes here."""

	def __init__(self, bot):
		self.bot = bot

	@commands.command(
		name='convite',
		help='Cria um convite para entrar na guilda. '
		     'Pode Receber os parâmetros: '
		     'Quantidade de usos, se não e unico se quer receber em DM')
	async def createInvite(self, ctx, max_uses='1', unique='True', public='True'):

		unique = True if re.search('([Ss]|[Yy]|True|true|[Tt])', unique) else False
		public = True if re.search('([Ss]|[Yy]|True|true|[Tt])', public) else False
		max_uses = int(max_uses)
		invitelink = await ctx.channel.create_invite(max_uses=max_uses, unique=unique)
		if public:
			await ctx.send(f'{seuConvite} {invitelink}')
		else:
			await ctx.author.send(f'{seuConvite} {invitelink}')

	async def cog_command_error(self, ctx, error):
		if isinstance(error, Exception):
			await ctx.send(f'Formate melhor os parâmetros que você quer me passar')


def setup(bot):
	bot.add_cog(Invite(bot))
