__author__ = 'airturk'

from stack import Stack

def dec2binFunc(quotient):

 # create a stack object
 s = Stack()

 # in a loop till the quotient is not equal to 1
 while quotient > 0:
     # divide by 2, push the remainder to stack, and keep the quotient, repeat
     s.push(quotient % 2)
     quotient /= 2

 # read from the stack and put it in a string
 bin_string = ""
 while not s.isEmpty():
     bin_string += str(s.pop())

 return bin_string


print dec2binFunc(14)

print dec2binFunc(102)

print dec2binFunc(56)