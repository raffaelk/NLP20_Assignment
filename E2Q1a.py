import numpy as np

# example string
string = 'ABBCBRTOBZEOCMSBA'

# number of chracters in the string
n = len(string)

# lookup table
table = np.zeros((n, n))

# iterate over possible substring lengths
for ssl in range(1, n+1):

    # iterate over possible start index of substring
    for i in range(n+1-ssl):

        # end index of substring
        j = i+ssl-1

        # a string of length 1 is always a palindrom of length 1
        if ssl == 1:
            table[i, j] = 1

        # find all palindrom of length 2
        elif ssl == 2 and string[i] == string[j]:
            table[i, j] = 2

        # find strings with equal start and end character
        elif string[i] == string[j]:
            table[i, j] = table[i+1, j-1] + 2

        # find string with different start and end character
        elif string[i] != string[j]:
            table[i, j] = max(table[i, j-1], table[i+1, j])

print(f'The length of the longest palindromic substring is: {table[0,-1]}')
