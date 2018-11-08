# Question: implement an algorithm to determine if a string has all unique characters. What if
# you cannot use additional data structures.

# if I could use a data structure I would use a hash table (key/value pairs through hashing func)

s = 'maybe'

add_data_structure = False

if add_data_structure:
    hash_table = {}
    # iterate over the letters of the string
    for c in s:

        # check the address
        if c in hash_table:
            # if there is an element already, string is not unique and exit
            print("Not a unique string")
            exit()
        else:
            # if there is no element, add the character
            hash_table[c] = c

    # if arrives here, announce that the string is unique

    print("A unique string")

else:
    # if I could not use another data structure, I use the iteration
    for i in range(0, len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                print("Not a unique string")
                exit()


    print("A unique string")

