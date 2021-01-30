from discord import utils


def find_channel(guild, channel='geral'):
	return utils.find(
		lambda g: g.name == channel, guild.text_channels
	)
