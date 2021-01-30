# -*- coding: utf-8 -*-
from discord.ext import commands

from utils.embed import create_embed
from utils.pets_urls import get_image_url


class Pet(commands.Cog):
	"""Manda foto de um cachorro ou de um gato"""

	def __init__(self, bot):
		self.bot = bot

	@commands.group(name='manda', aliases=['envia', 'send'])
	async def manda(self, ctx):
		petsPerm = ['cats', 'dogs']
		if ctx.subcommand_passed is None:
			await ctx.send('Pode enviar junto com manda: dogs, cats')
		elif ctx.subcommand_passed not in petsPerm:
			await ctx.send('No momento só posso te enviar dogs ou cats')

	@manda.command(name='dogs')
	async def dogs(self, ctx):
		url = get_image_url(1)
		embed = create_embed(
			autorName='Dog',
			icon_url=url,
			img_url=url,
			footer='Dog'
		)
		await ctx.send(embed=embed)

	@manda.command(name='cats')
	async def cats(self, ctx):
		url = get_image_url(2)
		embed = create_embed(
			autorName='Cats',
			icon_url=url,
			img_url=url,
			footer='Cats'
		)
		await ctx.send(embed=embed)


def setup(bot):
	bot.add_cog(Pet(bot))
