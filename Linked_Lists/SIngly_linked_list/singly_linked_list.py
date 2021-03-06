"""
What are singly linked lists?
In this tutorial, we will learn about what singly linked
lists are and some very basic operations that can be performed on them.

Before we get into the details of what singly lists are,
we must learn what nodes are. This is because nodes are the building blocks of a linked list. A node consists of two parts:

Data part - contains the data
Address part - this is pointer that points to location of the next node
In a singly linked list, each node’s address part contains the information about the location of the next node.
This forms a series of chain or links. The first node of the linked list is kept track by the head pointer. The last node points to None.

"""

class Node(object):

    def __init__(self,value):
        self.value =  value
        self.nextNode = None



a = Node(1)
b = Node(2)
c = Node(3)

a.nextNode = b
b.nextNode = c
print(a.nextNode.value)
print(b.nextNode.value)
"""
Advantages

It’s a dynamic data structure in which insertion and deletion are simple as we don’t need to shift the elements. 
Just updating the next pointer will do the job for us.
Stack and Queue data structures can be easily implemented using linked lists.
Disadvantages

Additional memory is used up by the next pointers.
Random access is not possible. You must traverse the linked list from the beginning to get to a particular node.
"""