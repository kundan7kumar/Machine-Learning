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