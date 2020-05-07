import re

import requests


def get_url():
	contents = requests.get('https://random.dog/woof.json').json()
	url = contents['url']
	print('get_url', url)
	return url


def get_image_url(self):
	allowed_extension = ['jpg', 'jpeg', 'png', 'gif']
	file_extension = ''
	while file_extension not in allowed_extension:
		url = self.get_url()
		print('get_img_url', url)
		file_extension = re.search("([^.]*)$", url).group(1).lower()
	return url
