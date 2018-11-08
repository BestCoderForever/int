# Question: Given two strings write a method to decide if one is a permutation of the other

solution_type = 'sort_first1'

def permutation_check_sort(str1, str2):

    if len(str1) != len(str2):
        print(False)
        exit()

    s1 = sorted(str1)

    s2 = sorted(str2)

    return s1 == s2

def permutation_check_rem(str1, str2):

    if len(str1) != len(str2):
        print(False)
        exit()

    # create a list
    list1 = list(str1)
    list2 = list(str2)

    for a1 in range(0, len(list1)):
        for a2 in range(0, len(list2)):
            if list1[a1] == list2[a2]:
                list1[a1] = ''
                list2[a2] = ''

    for c in list1:
        if c != '':
            print(False)
            exit()

    for c in list2:
        if c != '':
            print(False)
            exit()

    return True

if solution_type == 'sort_first':
    print(permutation_check('ali', 'irturk'))
else:
    print(permutation_check_rem('radar', 'darda'))