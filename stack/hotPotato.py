from queue_homemade import QueueNew

# Names of the kids
names = ['Bill', 'David', 'Susan',
         'Jane', 'Kent', 'Brad']

# number of enqueu and dequeue operations
num = 2

# Create a new queue
q = QueueNew()

# take the list and add them to the queue
for name in names:
    print(name)
    q.enqueue(name)

# until 1 name left in the list
while q.size() > 1:

    # in a loop perform num dequeue/enqueue operations
    for i in range(0,num):
        q.enqueue(q.dequeue())

    # remove the one from the queue
    q.dequeue()

print('only person left is %s' %q.dequeue())