import os
from pathlib import Path  # python3 only

from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

token = os.getenv('TOKEN')
url_janet_photo = os.getenv('URL_JANET_PHOTO')
wiki_photo = os.getenv('WIKI_PHOTO')

# cogs
cogs = [
	'cogs.Greetings',
	'cogs.Invite',
	'cogs.Pet',
	'cogs.Wiki',
	'cogs.Help'
]
