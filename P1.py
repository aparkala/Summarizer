from algorithms import textRank
from utils import textModify
from utils.graph import TextGraph
from textUnit.sentence import SentenceUnit

import re
import sys

def summary(text):


	cleanText = textModify.initCleaner(text)
	sentences = textModify.getSentences(cleanText)

	#for index,sentence in enumerate(sentenceObjects):
	#	print(index, "\n", "----------------------", "\n", sentence.tokens)


	sentenceObjects = []

	#create sentence objects
	for sentence in sentences:
		if re.search(r'\w',sentence):
			if len(sentence.split(" ")) < 4:
				continue
			sentenceObjects.append(SentenceUnit(sentence))



	#create a graph
	textGraph = TextGraph(sentenceObjects)

	#perform textRank
	summary = textRank.summarize(textGraph)

	return summary

	"""
	#INPUT TEXT FROM STDIN
	text = sys.stdin.read()
	cleanText = textModify.initCleaner(text)

	#get sentences
	sentences = textModify.getSentences(cleanText)
	"""
