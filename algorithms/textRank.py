import config

def summarize(textGraph):
	graph = textGraph.graph
	numberOfVertices = textGraph.numberOfVertices

	rankedGraph, vertexScores = rank(graph, numberOfVertices)

	summarySize = int(numberOfVertices / config.TEXT_TO_SUMMARY_RATIO)

	vertexScores.sort(reverse = True)
	minScore = vertexScores[summarySize]

	summary = ""

	for vertex, attribute in graph.items():
		if (attribute[0] >= minScore):
			summary += str(attribute[1])
			if len(summary.split(" ")) > config.MAX_WORDS:
				break

	return summary

def rank(graph, numberOfVertices):

	verticesAboveThreshold = []
	vertexScores = []
	iteration = 0

	while(True):
		iteration += 1
		for vertex, attribute in graph.items():
			vertexStrength = 0
			oldScore = attribute[0]

			for neighbour in attribute[2]:
				vertexStrength += getNeighbourStrength(neighbour[0], neighbour[1], graph)

			newScore = (1 - config.DAMPING_FACTOR) + (config.DAMPING_FACTOR * vertexStrength)

			if abs(newScore - oldScore) <= config.THRESHOLD:
				if vertex not in verticesAboveThreshold:
					verticesAboveThreshold.append(vertex)
					vertexScores.append(oldScore)

			else:
				attribute[0] = newScore

		if (len(verticesAboveThreshold) == numberOfVertices) or (iteration == 100):
			break

	return (graph, vertexScores)

	


def getNeighbourStrength(neighbour, cxnWeight, graph):
	neighbourScore = graph[neighbour][0]

	neighbourStrength = 0
	for cxn in graph[neighbour][2]:
		neighbourStrength += cxn[1]

	return neighbourScore * cxnWeight / neighbourStrength





