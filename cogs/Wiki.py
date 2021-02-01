# -*- coding: utf-8 -*-
from discord.ext import commands
from utils.embed import formatWikiaEmbed, listEmbed
from config import wiki_photo
from texts.ptbr import wait, ambiguities, ambiguitiesDescriptions
import wikipedia
import random
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
				toSearch = ctx.subcommand_passed.strip()
				toSearch = toSearch.replace('_', '%20')
				page = wikipedia.page(toSearch)
				embed = formatWikiaEmbed(page, wiki_photo)
			except wikipedia.exceptions.DisambiguationError as e:
				embed = listEmbed(
					list=e.options,
					listTitle=f'{ambiguities} para {ctx.subcommand_passed}',
					autorName='wiki',
					photo=wiki_photo,
					title=ambiguities,
					discription=ambiguitiesDescriptions
				)
				return await ctx.send(embed=embed)
			except wikipedia.exceptions.PageError as e:
				print(e)
				return await ctx.send(f'Desculpe não encontrei oque você procura')
		else:
			randomSearch = wikipedia.random()
			randomSearch.replace(' ', '%20')
			print(randomSearch)
			page = wikipedia.page(randomSearch)
			embed = formatWikiaEmbed(page, wiki_photo)
		return await ctx.send(embed=embed)

	async def cog_command_error(self, ctx, error):
		print(error)
		if isinstance(error, Exception):
			await ctx.send(f'Ops... Algo deu errado')


def setup(bot):
	bot.add_cog(Wiki(bot))
