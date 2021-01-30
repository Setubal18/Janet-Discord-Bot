def urlImg(**kwards):
	print(kwards)


def formatSuggestionUrl(suggestions):
	urls = []
	for suggestion in suggestions:
		urls.push(suggestion.replace(' ', '_'))
	return urls
