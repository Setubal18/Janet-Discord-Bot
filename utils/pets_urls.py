import re

import requests


def get_url_dog():
	contents = requests.get('https://random.dog/woof.json').json()
	return contents['url']


def get_url_cat():
	content = requests.get('http://aws.random.cat/meow').json()
	return content['file']


def get_image_url(animal):
	allowed_extension = ['jpg', 'jpeg', 'png', 'gif']
	file_extension = ''
	while file_extension not in allowed_extension:
		if animal == 1:
			url = get_url_dog()
		elif animal == 2:
			url = get_url_cat()
		file_extension = re.search("([^.]*)$", url).group(1).lower()
	return url
