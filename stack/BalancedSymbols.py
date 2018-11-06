__author__ = 'airturk'

from stack import Stack

# create a stack object
s = Stack()

# create a sample string with symbols include ([{ }])
symbols = "}({[]}){"

# Balanced Flag
isBalanced = True

# Create a dictionary for lookup
matchingDict = {
    "}" : "{",
    ")" : "(",
    "]" : "["
}

for symbol in symbols:
    if symbol in "({[":
        s.push(symbol)
    elif symbol in ")}]":
        if not(s.isEmpty()):
            topStack = s.pop()
        else:
            print "Unbalanced because the stack is empty"
            isBalanced = False
            break
        if matchingDict[symbol] != topStack:
            print "Unbalanced"
            isBalanced = False
            break
    else:
        print "Some unexpected text was entered!"

print ('The balance of the system is %r' % isBalanced)






