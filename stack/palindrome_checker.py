__author__ = 'airturk'

from deque_homemade import Deque


def check(word):

    # Create a deque
    d = Deque()

    # Push all the letters in a deque
    for letter in word:
        d.add_front(letter)

    # loop till the number of elements is smaller than 2
    while d.size() > 1:

        # remove from both ends of the deque and compare
        if d.remove_front() == d.remove_back():
            # if same continue
            print('letters are same, Good!')
        else:
            # else break and call it not a palindrome
            print('not a palidrome')
            quit()

    print("the word is palindrome")


# sample code

check('notradar')
print("finished")