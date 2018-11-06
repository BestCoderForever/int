__author__ = 'ali.irturk'

# step 1 is to define the abstract data type for queue

# Queue() -> create a new queue that is empty, returns the queue
# enqueue(item) -> add item in the queue, returns nothing
# dequeue() -> remove an item from the queue, return the item
# isEmpty() -> check to see if the queue is empty, print True if it is empty, and False if not empty
# size() -> print the size of the queue

class QueueNew():

    def __init__(self):
        self.q = [] # create an empty list

    def enqueue(self, item):
        # add the item in the queue
        self.q.append(item)

    def dequeue(self):
        # remove the item from the queue
        return self.q.pop(0)

    def isEmpty(self):
        print(self.q == [])

    def size(self):
        print(len(self.q))
        return len(self.q)

    def peek_elements(self):
        return self.q

# Test code starts here
#s = QueueNew()

#s.isEmpty()

#s.size()

#s.enqueue('ALI')

#s.enqueue('VELI')

#s.enqueue("49")

#s.enqueue("50")

#print(s.dequeue())

#print(s.dequeue())

#s.isEmpty()

#s.size()

#print(s.dequeue())

#s.isEmpty()

#s.size()