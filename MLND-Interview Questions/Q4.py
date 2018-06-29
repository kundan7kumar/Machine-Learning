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
#Space Complexity =O(h) where h height of the binary tree



