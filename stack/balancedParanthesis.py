__author__ = 'airturk'

#import the stack class
from stack import Stack
# create a stack called s
s = Stack()

# create sample input data
input = "()()(((()))()()"

# loop over the input and push/pop to the s
for n in range(len(input)):
    if input[n] == "(":
        s.push('(')
    elif input[n] == ")":
        s.pop()
    else:
        print "Something went wrong!"

# once complete check to see if empty. If yes, balanced. If not, not balanced.
if s.isEmpty():
    print "It is balanced!"
else:
    print "It is not balanced!"










