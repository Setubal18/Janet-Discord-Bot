import discord

from config import url_janet_photo


def create_embed(**kwargs):
	embed = discord.Embed()

	try:
		embed.set_author(name=kwargs['autorName'], icon_url=kwargs['url'])
	except KeyError:
		embed.set_author(name='Janet', icon_url=url_janet_photo)

	try:
		embed.set_image(url=kwargs['url'])
	except KeyError:
		embed.Empty()

	try:
		embed.set_footer(text=kwargs['footer'])
	except KeyError:
		embed.set_footer(text='')

	return embed
