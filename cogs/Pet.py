# -*- coding: utf-8 -*-

from discord.ext import commands

from utils.pets_urls import get_image_url


class Pet(commands.Cog):
	"""The description for Pet goes here."""

	def __init__(self, bot):
		self.bot = bot

	@commands.group(name='manda', aliases=['envia'])
	async def manda(self, ctx):
		if ctx.subcommand_passed is None:
			await ctx.send('Pode enviar junto com manda: dogs, cats')

	# if ctx.subcommand_passed != 'dogs' or 'cats':
	# 	await ctx.send('No momento só posso te enviar dogs ou cats')

	@manda.command(name='dogs')
	async def dogs(self, ctx):
		url = get_image_url()
		await ctx.send(f'Aqui está: {url}')


def setup(bot):
	bot.add_cog(Pet(bot))
