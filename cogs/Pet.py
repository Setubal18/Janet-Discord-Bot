# -*- coding: utf-8 -*-

from discord.ext import commands


class Pet(commands.Cog):
	"""The description for Pet goes here."""

	def __init__(self, bot):
		self.bot = bot


def setup(bot):
	bot.add_cog(Pet(bot))
