# -*- coding: utf-8 -*-

from discord.ext import commands
from utils.embed import create_embed
from discord import embeds
import discord
from texts.ptbr import help


class Help(commands.Cog):
	"""The description for Help goes here."""

	def __init__(self, bot):
		self.bot = bot

	@commands.group(invoke_without_command=True)
	async def help(self, ctx):
		helpdict = help[0]
		if (ctx.subcommand_passed != None):
			return
		else:
			embed = create_embed(
				title=helpdict['title']['title'],
				description=helpdict['title']['description'],
				fields=[helpdict['commands']],
			)
			return await ctx.send(embed=embed)

	@help.command()
	async def wiki(self, ctx):
		helpdict = help[0]
		embed = create_embed(
			title=helpdict['wiki']['title'],
			description=helpdict['wiki']['description'],
			fields=[helpdict['wiki']],
		)
		await ctx.send(embed=embed)

	@help.command()
	async def pet(self, ctx):
		helpdict = help[0]
		embed = create_embed(
			title=helpdict['pet']['title'],
			description=helpdict['pet']['description'],
			fields=[helpdict['pet']],
		)
		await ctx.send(embed=embed)

	@help.command()
	async def invite(self, ctx):
		helpdict = help[0]
		embed = create_embed(
			title=helpdict['invite']['title'],
			description=helpdict['invite']['description'],
			fields=[helpdict['invite']],
		)
		await ctx.send(embed=embed)

	@help.command()
	async def greetings(self, ctx):
		helpdict = help[0]
		embed = create_embed(
			title=helpdict['greetings']['title'],
			description=helpdict['greetings']['description'],
			fields=helpdict['fields'],
		)
		await ctx.send(embed=embed)


def setup(bot):
	bot.add_cog(Help(bot))
