# Question: Implement a method to perform basic string compression using the counts of repeated
# characters. For example, the string aabcccccaaa would become a2b1c5a3. If the compressed string
# wouldn't become smaller than the original string, your method should return the original.


# Assumptions:
# 'a' and 'A' are different characters
# Assume ASCII character set [0, 255]
# This is huffman encoding

# create a function that receives the string
def compress(string):

    # initialize a counter to 0 and temp variable to Null and create an empty string
    counter = 0
    temp = None
    c_string = ''

    # loop over the string picking one character at a time
    for c in string:
        # if temp variable is null
        if temp == None:
            # copy the character to the temp variable and increment the counter
            temp = c
            counter  = counter + 1
        # else
        else:
            # compare the new character to the temp variable
            # if the temp and new character are same
            if c == temp:
                # increment counter
                counter = counter + 1
                # else
            else:
                # append temp and counter to the empty string
                c_string = c_string + temp + str(counter)
                # temp becomes the new character and counter goes to 1
                temp = c
                counter = 1

    c_string = c_string + temp + str(counter)

    # compare the length of the uncompressed and compressed strings
    if  len(string) > len(c_string):
        return c_string
    else:
        return string


print(compress("aabcccccaaa"))
