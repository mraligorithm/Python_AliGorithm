"""
A stack is an ordered collection of items where the addition of new items and the removal
of existing items always takes place at the same end. This end is commonly referred to as
the “top.” The end opposite the top is known as the “base.”

The base of the stack is significant since items stored in the stack that are closer to the
base represent those that have been in the stack the longest. The most recently added item is
the one that is in position to be removed first.

This ordering principle is sometimes called LIFO, last-in first-out. It provides an ordering
based on length of time in the collection. Newer items are near the top, while older items are near the base.

Implementation of Stack
Stack Attributes and Methods
Before we implement our own Stack class, let's review the properties and methods of a Stack.

The stack abstract data type is defined by the following structure and operations.
A stack is structured, as described above, as an ordered collection of items where
items are added to and removed from the end called the “top.” Stacks are ordered LIFO.
The stack operations are given below.

Stack() creates a new stack that is empty. It needs no parameters and returns an empty stack.
push(item) adds a new item to the top of the stack. It needs the item and returns nothing.
pop() removes the top item from the stack. It needs no parameters and returns the item. The stack is modified.
peek() returns the top item from the stack but does not remove it. It needs no parameters. The stack is not modified.
isEmpty() tests to see whether the stack is empty. It needs no parameters and returns a boolean value.
size() returns the number of items on the stack. It needs no parameters and returns an integer.
"""
class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)





from nose.tools import assert_equal


class TestStack:

    def testEmpty(self, stack):
        assert_equal(stack.isEmpty(), True)
        print("Test Passed")


    def testContains(self,stack):
        assert_equal(stack.size(), 1)
        print("SecondTestPasses")


s = Stack()
t = TestStack()
t.testEmpty(s)
s.push(4)
t.testContains(s)
s.pop()
t.testEmpty(s)