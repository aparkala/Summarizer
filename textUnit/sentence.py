from utils.textModify import tokenize

#from textCleaner import cleanTokens

class SentenceUnit:
	def __init__(self, text = None, tokens = None):
		self.text = text
		self.tokens = []
		self.generateTokens()
		return

	def __str__(self):
		return self.text

	def generateTokens(self):
		self.tokens = tokenize(self.text)
		return