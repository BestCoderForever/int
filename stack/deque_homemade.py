__author__ = 'ali.irturk'

# Definition of the abstract data type

# Dequeu() -> creates a empty deque
# add_front(item) -> allows user to add an item to the front of the deque
# remove_from -> allows user to remove an item from the front of the deque, and return it
# add_back(item) -> allows user to add an item to the back of the deque
# remove_back() -> allows user to remove an item from the back of the deque
# isEmpty() -> returns True if the deque is empty, false otherwise
# size() -> returns the size of the deque


class Deque:

    def __init__(self):
        self.dq = [] # create an empty list

    def add_front(self, item):
        self.dq.append(item)

    def remove_front(self):
        return self.dq.pop()

    def add_back(self, item):
        self.dq.insert(0, item)

    def remove_back(self):
        return self.dq.pop(0)

    def isEmpty(self):
        print(self.dq == [])

    def size(self):
        print(len(self.dq))
        return len(self.dq)

#dq = Deque()
#dq.isEmpty()
#dq.size()

#dq.add_front('100')
#dq.add_front('101')
#dq.add_front('102')
#dq.add_back('200')
#dq.add_back('201')
#dq.add_back('202')

#dq.remove_back()
#dq.remove_front()

#dq.remove_back()
#dq.remove_front()
