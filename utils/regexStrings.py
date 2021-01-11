
#REGEX to remove periods from abbreviations 
RE_ABBREVIATION = r'(?<!\w)([A-Z])\.'
RE_ABBREVIATION_SUB = r'\1'

#REGEX to extract sentences
RE_SENTENCE = '(\S.+?[.!?])(?=\s+|$)|(\S.+?)(?=[\n]|$)'

#REGEX to convert "e.g." -> "for example"
RE_EXAMPLE = r'e\.g\.?'
RE_EXAMPLE_SUB = r', for example,'

#REGEX to convert time suffixes
RE_AM_PM = {
	r'a\.m\.?': r'A.M.',
	r'p\.m\.?': r'P.M.'
}

#REGEX to remove periods from common salutations
RE_SALUTATIONS = {
	r'Mr\.': r'Mr',
	r'Ms\.': r'Ms',
	r'Dr\.': r'Dr',
	r'Mrs\.': r'Mrs',
	r'Prof\.': r'Professor'
}

#REGEX to remove punctuations
RE_PUNCT = r'^(\W*)(\w+)(\W)?(\w*)(\W*)$'
RE_PUNCT_SUB_PRE = r'\2'
RE_PUNCT_SUB_POST = r'\4'