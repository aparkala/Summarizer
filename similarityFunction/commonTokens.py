from math import log


def similarityScore(vertexTokens, neighbourTokens):
	vertexTokenSet = set(vertexTokens)
	neighbourTokenSet = set(neighbourTokens)

	if log(len(vertexTokenSet)) + log(len(neighbourTokenSet)) == 0:
		return 0

	commonTokens = vertexTokenSet.intersection(neighbourTokenSet)

	similarityScore = len(commonTokens)/(log(len(vertexTokenSet)) + log(len(neighbourTokenSet)))

	return similarityScore


