__author__ = 'airturk'

# step 1 is to define the abstract data type (ADT) for stack

# stack() -> create a new stack that is empty
# push(item) -> add an item to the stack, it will be on the top
# pop() -> returns the item at the top by removing the item at the top
# peek() -> returns the item at the top, but doesn't remove it
# isEmpty() -> return True if the stack is empty, False otherwise
# size() -> returns the size of the stack

# Implementation of the data structure by creating a new class

class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


s = Stack()
#
print(s.isEmpty())
# s.push(4)
# s.push('dog')
# print(s.peek())
# s.push(True)
# print(s.size())
# print(s.isEmpty())
# s.push(8.4)
# print(s.pop())
# print(s.pop())
# print(s.size())




