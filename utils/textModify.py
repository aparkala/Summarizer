import re
from utils import regexStrings
from utils.stopWords import stopWords

def initCleaner(text):
	for key, value in regexStrings.RE_AM_PM.items():
		text = re.sub(key,value,text)
		#print(text)

	#convert "e.g." to "for example"
	text = re.sub(regexStrings.RE_EXAMPLE, regexStrings.RE_EXAMPLE_SUB, text)

	#fix abbreviations in text: U.S. -> US, A.M. -> AM
	text = re.sub(regexStrings.RE_ABBREVIATION, regexStrings.RE_ABBREVIATION_SUB, text)
	#print(text)

	#fix salutations in text
	for key,value in regexStrings.RE_SALUTATIONS.items():
		text = re.sub(key,value,text)
		#print(text)

	return text


def getSentences(text):
	sentences = []
	#print(text)

	for sentence in re.findall(regexStrings.RE_SENTENCE, text):
		sentences.append(sentence[0])

	return sentences


def tokenize(text):
	tokens = []
	
	for word in text.split(" "):
		if re.search(r'\W', word): 
			tokens.extend(cleanPunctuation(word))

		else:
			if word.lower() not in stopWords:
				tokens.append(word.lower())

	return tokens

def cleanPunctuation(text):
	prePunctuation = re.sub(regexStrings.RE_PUNCT, regexStrings.RE_PUNCT_SUB_PRE, text)
	postPunctuation = re.sub(regexStrings.RE_PUNCT, regexStrings.RE_PUNCT_SUB_POST, text)

	cleanWords = []

	if postPunctuation:
		if postPunctuation.lower() not in stopWords:
			cleanWords.append(postPunctuation.lower())

	if prePunctuation.lower() not in stopWords:
		cleanWords.append(prePunctuation.lower())

	return cleanWords









