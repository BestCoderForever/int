# Question: Implement a MyQueue Class which implements a queue using two stacks

class MyStack:

    def __init__(self):
        self.s = [] # create an empty list as a stack

    def push(self, item):
        self.s.append(item)

    def pop(self):
        return self.s.pop()

    def size(self):
        return len(self.s)

    def isEmpty(self):
        return self.s == []


class MyQueue(MyStack):

    def __init__(self):
        self.s1 = MyStack()
        self.s2 = MyStack()

    def enqueue(self, item):
        self.s1.push(item)

    def dequeue(self):

        while not self.s1.isEmpty():
            self.s2.push(self.s1.pop())


        return_value = self.s2.pop()

        while not self.s2.isEmpty():
            self.s1.push(self.s2.pop())

        return return_value


#### MyQueue ####

q = MyQueue()

q.enqueue(10)

q.enqueue(20)

q.enqueue(30)

q.dequeue()

q.enqueue(100)

print(q.dequeue())

q.enqueue(120)

#### Test Stack  ####
#s = MyStack()

#print(s.isEmpty())

#s.push(10)

#print(s.isEmpty())

#s.push(20)

#print(s.size())

#s.pop()

#print(s.size())
