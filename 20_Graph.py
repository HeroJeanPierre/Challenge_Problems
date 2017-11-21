class Vertex:
	def __init__(self, name):
		self.name = name
		self.neighbors = list()

	def add_neighbor(self, v):
		if v not in self.neighbors:
			self.neighbors.append(v)
			self.neighbors.sort()


class Graph:
	def __init__(self):
		self.vertices = {}

	def add_vertex(self, vertex):
		if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
			self.vertices[vertex.name] = vertex
			return True
		else:
			return False

	def add_edge(self, u, v):
		if u in self.vertices and v in self.vertices and v != u:

			for key, value in self.vertices.items():
				if key == u:
					value.add_neighbor(v)
				if key == v:
					value.add_neighbor(u)

			return True
		else:
			return False

	def print_graph(self):
		for key in sorted(list(self.vertices.keys())):
			print key + " : " + str(self.vertices[key].neighbors)

g = Graph()

for i in range(ord('A'), ord('Z') + 1):
	g.add_vertex(Vertex(chr(i)))


from random import randint

for _ in range(10):

	g.add_edge(chr(ord('A') + randint(0, 26)), chr(ord('A') + randint(0, 26)))

g.print_graph()