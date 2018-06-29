# Question 3
# Given an undirected graph G, find the minimum spanning tree within G.
# A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges.
# Your function should take in and return an adjacency list structured like this:

# {'A': [('B', 2)],
# 'B': [('A', 2), ('C', 5)],
# 'C': [('B', 5)]}
# Vertices are represented as unique strings. The function definition should be question3(G)

# This question is answered by finding the minimum spanning tree of the graph.
# To do this, Prim's algorithm will be used.
#
# class Graph:
# 	def __init__(self, vertices):
# 		self.V = vertices  # No. of vertices
# 		self.graph = []

parent = dict()
rank = dict()

def make_set(v):
    parent[v] = v
    rank[v] = 0

# function to find vertex
def find(vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent[vertex])
    return parent[vertex]


# Function for union of two vertices based on  rank)
def union(v1, v2):
    root1 = find(v1)
    root2 = find(v2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
			# if rank are same ,make it as root and increment it
            if rank[root1] == rank[root2]:rank[root2] += 1


def question3(graph):
    for vertices in graph.keys():
        make_set(vertices)

	#create a dictionary for minimum spanning tree
    min_span_tree = {}

    edges = []
    for key in graph:
        for element in graph[key]:
            edges.append((element[1], key, element[0]))

    edges.sort()
    for edge in edges:
        wi, v1, v2 = edge
		# check vertices
        if find(v1) != find(v2):
            union(v1, v2)

            if v1 in min_span_tree:
                min_span_tree[v1].append((v2, wi))
            else:
                min_span_tree[v1] = [(v2, wi)]

            if v2 in min_span_tree:
                min_span_tree[v2].append((v1, wi))
            else:
                min_span_tree[v2] = [(v1, wi)]
    return min_span_tree

print (question3({'A': [('B', 3), ('E', 1)],
                 'B': [('A', 3), ('C', 9), ('D', 2), ('E', 2)],
                 'C': [('B', 9), ('D', 3), ('E', 7)],
                 'D': [('B', 2), ('C', 3)],
                 'E': [('A', 1), ('B', 2), ('C', 7)]}))
# will print
# {'A': [('E', 1)],
#  'C': [('D', 3)],
#  'B': [('E', 2), ('D', 2)],
#  'E': [('A', 1), ('B', 2)],
#  'D': [('B', 2), ('C', 3)]}

print (question3({}))
# will print {}

print (question3({'A': [('B', 7), ('D', 5)],
                 'B': [('A', 7), ('C', 8), ('D', 9), ('E', 7)],
                 'C': [('B', 8), ('E', 5)],
                 'D': [('A', 5), ('B', 9), ('E', 15), ('F', 6)],
                 'E': [('B', 7), ('C', 5), ('D', 15), ('F', 8), ('G', 9)],
                 'F': [('D', 6), ('E', 8),  ('G', 11)],
                 'G': [('E', 9), ('F', 11)]}))

# will print
# {'A': [('D', 5), ('B', 7)],
#  'C': [('E', 5)],
#  'B': [('A', 7), ('E', 7)],
#  'E': [('B', 7), ('C', 5), ('G', 9)],
#  'D': [('A', 5), ('F', 6)],
#  'G': [('E', 9)],
#  'F': [('D', 6)]}

#Time Complexity=O(E*V)
#Space Complexity=O(V) , where E is edges and V is vertices of the graph