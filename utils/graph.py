from similarityFunction import commonTokens

class TextGraph:

	def __init__(self, sentences = None):
		self.graph = {}
		self.numberOfVertices = len(sentences)

		for index, sentence in enumerate(sentences):
			self.graph[index] = [1, sentence, []]

		self.generateEdges()
		return

	def generateEdges(self):

		for vertex in self.graph.keys():

			for neighbour in range(vertex + 1, self.numberOfVertices):

				similarityScore = commonTokens.similarityScore(self.graph[vertex][1].tokens, self.graph[neighbour][1].tokens)

				if similarityScore == 0:
					continue
				else:
					self.graph[vertex][2].append([neighbour, similarityScore])
					self.graph[neighbour][2].append([vertex, similarityScore])

		return









