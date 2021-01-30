from datetime import datetime

import discord
from config import url_janet_photo


def create_embed(**kwargs):
	embed = discord.Embed()

	try:
		embed.set_author(name=kwargs['autorName'], icon_url=kwargs['icon_url'])
	except KeyError:
		embed.set_author(name='Janet', icon_url=url_janet_photo)

	try:
		embed.set_image(url=kwargs['img_url'])
	except KeyError:
		pass

	try:
		for field in kwargs['fields']:
			try:
				embed.add_field(
					name=field['name'],
					value=field['value'],
					inline=field['inline']
				)
			except KeyError:
				embed.add_field(
					name=field['name'],
					value=field['value'],
				)
	except KeyError:
		pass

	try:
		embed.set_footer(text=kwargs['footer'])
		embed.timestamp = datetime.now()
	except KeyError:
		pass

	return embed


def formatWikiaEmbed(page, wiki_photo):
	paragraph = page.summary.split('\n')[0]
	font = f'\n [Fonte]({page.url})'
	paragraph = paragraph + font
	embed = create_embed(
		autorName='Wiki',
		icon_url=wiki_photo,
		title=page.title,
		fields=[
			{
				'name': page.title,
				'value': paragraph,
				'inline': False
			}
		],
		footer='By Janet'
	)

	return embed


def listEmbed(**kwargs):
	list: list = []
	value = ''
	for item in kwargs['list']:
		if len(value) <= 1000:
			value += f'- {item}\n'
		else:
			list.append({'name': kwargs['listTitle'], 'value': value, 'inline': False})
			value = ''
	embed = create_embed(
		autorName=kwargs['autorName'],
		icon_url=kwargs['photo'],
		title=kwargs['title'],
		fields=list,
		footer='By Janet'
	)

	return embed
