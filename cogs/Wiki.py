# -*- coding: utf-8 -*-

from discord.ext import commands
from utils.embed import create_embed
from config import wiki_photo
import wikipedia
import discord


class Wiki(commands.Cog):
	"""Pesquisa alguma informação na wikia"""

	def __init__(self, bot):
		self.bot = bot

	@commands.group(name='wiki', aliases=['pesquisar', 'search', 'find'])
	async def wiki(self, ctx):
		page = wikipedia.page(ctx.subcommand_passed)
		paragraph = page.summary.split('\n')[0]
		font = "\n [Fonte]({})".format(page.url)
		paragraph = paragraph + font
		embed = create_embed(
			autorName="Wiki",
			icon_url=wiki_photo,
			title=page.title,
			fields=[
				{
					"name": page.title,
					"value": paragraph,
					"inline": False
				}
			],
			footer='By Janet'
		)

		await ctx.send(embed=embed)


def setup(bot):
	bot.add_cog(Wiki(bot))
