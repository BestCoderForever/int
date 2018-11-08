# Question: Write a program to sort a stack in ascending order (with biggest items on top). You
# may use at most one additional stack to hold items, but you may not copy the elements into any other
# data structure (such as an array). The stack supports the following operations: push, pop,
# peek and isEmpty.


class MyStack():

    def __init__(self):
        self.s = []

    def push(self, item):
        self.s.append(item)

    def pop(self):
        return self.s.pop()

    def peek(self):
        return self.s[len(self.s)-1]

    def isEmpty(self):
        return self.s == []


def sort_stack(aStack):

    tStack = MyStack()

    tStack.push(aStack.pop())

    while not aStack.isEmpty():

        a = aStack.pop()

        while (not tStack.isEmpty() and a < tStack.peek()):
            aStack.push(tStack.pop())

        tStack.push(a)

    return tStack

my = MyStack()

my.push(34)
my.push(3)
my.push(31)
my.push(98)
my.push(92)
my.push(23)
print(my.peek())

result = sort_stack(my)

print('ali')