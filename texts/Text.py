import re
import ptbr
class Text:
	def __init__(self, language):
		self.language = language

	def getlanguage(self):
		return language

	def setlanguage(self, language):
		self.language = language

	def getText(self,text):
		return translate(getlanguage(), text)

	def translate(self, language, phrase):
		try:
			if language in re.search('([ptPT]|[brBR])'):
				return ptbr.phrase
		except:
			pass