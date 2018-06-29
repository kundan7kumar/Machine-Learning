#Question 1
'''Given two strings s and t, determine whether some anagram of t is a substring of s.
 For example: if s = "udacity" and t = "ad", then the function returns True.
Your function definition should look like: question1(s, t) and return a boolean True or False'''

def question1(s,t):

    #check string s and string t are equals
    if s==t:
        return True

    # if either of strings( s and t) is null
    if s==None or t==None:
        return False

    # for t should be substring of s . length of t should be smaller than s
    if len(t)>len(s):
        return False

    # Checking the character of t in s
    s=s.lower()
    t=t.lower()
    for character in t:
        if character in s:
            s = s.replace(character, '')
            t = t.replace(character, '')
    if not t:
        return True
    return False


# Test cases
print (question1("udAcity"," "))
print (question1(" "," "))
print (question1(" ","city"))
print (question1("udaCiTy","city"))
print (question1("udacity","ad"))


#Time Complexity =O(N) N is the number of element in the string
#Space Complexity =O(1)


# Question 2
# Given a string a, find the longest palindromic substring contained in a.
# Your function definition should look like question2(a), and return a string.
# NOTE: For quetions 1 and 2 it might be useful to have a function that returns all substrings...
# Check string is Palindrome or not
def isPal(s):
	# If string s is empty
	if not s:
		return True

	#if len of string is 1
	if len(s) == 1:
		return True

	# Else check the string is Palindrome
	if s[0] == s[-1]:
		return isPal(s[1:-1])
	return False


def question2(a):
	long_pal = ''

	# Check the string is palindrome
	if isPal(a):
		return a

	# Check all substrings whether it is palindrome.If palindrome and larger than longest_pal
	# make longest_pal the current substring
	i = len(a)
	j = 0
	while j != i:
		while i != j:

			if len( a[j:i] ) >= len( long_pal ) and isPal( a[j:i] ):
				long_pal = a[j:i]
			i=i- 1

		j =j+1
		i = len(a)

	return long_pal


# Test cases
print (question2("abcba"))
print (question2("forgeeksskeegfor"))
print (question2("a"))
print (question2(" "))
print (question2("qwertyyterq"))

#Time Complexity =O(N^2) where N length of string a
#Space Complexity =O(1)


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

#Time Complexity=O(ElogE)
#Space Complexity=O(V) , where E is edges and V is vertices of the graph

#Question 4
# Find the least common ancestor between two nodes on a binary search tree.
# The least common ancestor is the farthest node from the root that is an ancestor of both nodes.
# For example, the root is a common ancestor of all nodes on the tree,
# but if both nodes are descendents of the root's left child,
# then that left child might be the lowest common ancestor.
# You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties.
# The function definition should look like question4(T, r, n1, n2), where T is the tree represented as a matrix,
# where the index of the list is equal to the integer stored in that node and a 1 represents a child node,
# r is a non-negative integer representing the root,
# and n1 and n2 are non-negative integers representing the two nodes in no particular order.
# For example, one test case might be

# question4([[0, 1, 0, 0, 0],
#            [0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0],
#            [1, 0, 0, 0, 1],
#            [0, 0, 0, 0, 0]],
#           3,
#           1,
#           4)
# and the answer would be 3.

def question4(T, r, n1, n2):

    n1p = []
    while n1 != r:
        n1 = root(T, n1)
        n1p.append(n1)

    if len(n1p) == 0:
        return T

    while n2 != r:
        n2 = root(T, n2)
        if n2 in n1p:
            return n2
    return -1


def root(T, n):
    # return root of n if it exists, otherwise return -1
    rows = len(T)
    for i in range(rows):
        if T[i][n] == 1:
            return i
    return -1


print (question4([[0, 1, 0, 0, 0],
				  [0, 0, 0, 0, 0],
				  [0, 0, 0, 0, 0],
				  [1, 0, 0, 0, 1],
				  [0, 0, 0, 0, 0]],
				 3,
				 1,
				 4))

print (question4([],
                None,
                None,
                None))

print (question4([[0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 1],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0]],
                  2,
                  3,
                  4))

#print (question4([[0]],0,0,0))
#Time Complexity =O(h)
#Space Complexity =O(h) where id height of the binary tree

#Question 5
'''Find the element in a singly linked list that's m elements from the end. For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element.
The function definition should look like question5(ll, m), where ll is the first node of a linked list and m is the "mth number from the end".  You should copy/paste the Node class below to use as a representation of a node in the linked list.
Return the value of the node at that position.'''
class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

def question5(ll, m):
    # Two pointer will start at same point rp(right pointer) ,lp(left pointer)
    rp = ll
    lp = ll

    # Set right pointer at m nodes away from head
    for i in range(0,m - 1):

        # Check for edge case of not having enough nodes
        if not rp.next:
            return 'm cannot be greater than linked list.'

        # Otherwise, update the right pointer
        rp = rp.next

    while rp.next:
        lp = lp.next
        rp = rp.next

    return lp.data


a = Node(1)
b = Node(2)
c = Node(6)
d = Node(5)
e = Node(4)
f = Node(2)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

print (question5(a,11)) # m cannot be greater than linked list
print(question5(a,1))   # print 2
print (question5(a,6))  # print 1
print (question5(a,2))  # print 4


#Time Complexity =O(N)
#Space Complexity =O(N) where N is the node of the linked list