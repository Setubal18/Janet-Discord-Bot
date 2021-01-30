# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from discord.ext import commands
from utils.embed import formatWikiaEmbed, listEmbed
from config import wiki_photo
from texts.ptbr import wait, ambiguities, ambiguitiesDescriptions
from wikipedia import exceptions, page

import random
import wikipedia
import discord


class Wiki(commands.Cog):
	'''Pesquisa alguma informação na wikia'''

	def __init__(self, bot):
		self.bot = bot

	@commands.group(name='wiki', aliases=['pesquisar', 'search', 'find'])
	async def wiki(self, ctx):
		global page, embed
		await ctx.send(random.choice(wait))
		if ctx.subcommand_passed:
			try:
				page = page(ctx.subcommand_passed)
				embed = formatWikiaEmbed(page, wiki_photo)
			except exceptions.DisambiguationError as e:
				embed = listEmbed(
					list=e.options,
					listTitle=f'{ambiguities} para {ctx.subcommand_passed}',
					autorName='wiki',
					photo=wiki_photo,
					title=ambiguities,
					discription=ambiguitiesDescriptions
				)
				return await ctx.send(embed=embed)
		else:
			page = page(wikipedia.random().replace(' ', '_'))
			embed = formatWikiaEmbed(page, wiki_photo)
		return await ctx.send(embed=embed)

	async def cog_command_error(self, ctx, error):
		if isinstance(error, Exception):
			await ctx.send(f'Desculpe não entendi oque você quer que eu procure 😢')


def setup(bot):
	bot.add_cog(Wiki(bot))
