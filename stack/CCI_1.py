# Question: How would you design a stack which in addition to push and pop, also has a function min
# which returns the minimum element. Push, pop and min should all operate in O(1) time.

__author__ = 'airturk'

# Define the abstract data type
# Stack() -> parameters: None, returns an empty stack
# push(item) -> parameters: item, returns nothing
# pop() -> parameters: None, return the item
# min() -> parameters: None, return the minimum element

class Stack():

    def __init__(self):
        self.s = []
        self.min_stack = []

    def push(self, item):

        if self.min_stack == []:
            self.min_stack.append(item)
        else:
            if self.min_stack[len(self.min_stack) - 1] > item:
                self.min_stack.append(item)
            else:
                self.min_stack.append(self.min_stack[len(self.min_stack) - 1])

        self.s.append(item)

    def pop(self):
        self.min_stack.pop()
        return self.s.pop()

    def min(self):
        return self.min_stack[len(self.min_stack) - 1]


stack = Stack()

stack.push(10)
stack.push(20)

print(stack.min())
stack.push(30)
stack.push(25)
stack.push(15)
stack.push(8)
stack.push(100)
stack.push(56)
print(stack.min())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.min())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.min())
print(stack.pop())
print(stack.min())
