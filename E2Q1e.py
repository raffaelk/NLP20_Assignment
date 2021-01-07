import numpy as np
import pandas as pd

# example string
string = 'AAABBBAAA'

# number of chracters in the string
n = len(string)

# lookup table
table = np.zeros((n, n))

# priority queue
pr_que = pd.DataFrame()

# initialize queue with all possible substings
for ssl in range(1, n+1):

    # iterate over possible start index of substring
    for i in range(n+1-ssl):

        # end index of substring
        j = i+ssl-1

        # assign priority 0 to all substrings
        idx = (i, j)
        value = 0
        pr_que = pr_que.append(pd.Series([idx, value]), ignore_index=True)

# iterate over priority queue untill the longest substring has been calculated
while table[0, -1] == 0:

    # get first element of priority queue
    i, j = pr_que.iloc[0, 0]

    # assign priority = lps to the substring
    if table[i, j] == 0 and pr_que.iloc[0, 1] > 0:
        table[i, j] = pr_que.iloc[0, 1]

    # next longer substring
    newj = j+1

    # substrings of length 1 get priority 1
    if i == j and table[i, j] == 0:
        idx = (i, j)
        value = 1
        pr_que.iloc[0, 1] = value

    # try to calculate the priority of the next longer substring
    elif newj < n and table[i, newj] == 0:

        # find palindrom of length 2
        if i == j and string[i] == string[newj]:
            idx = (i, newj)
            value = 2
            pr_que = pr_que.append(pd.Series([idx, value]), ignore_index=True)
            pr_que.drop(index=0, inplace=True)

        # find strings with equal start and end character
        elif string[i] == string[newj] and table[i+1, newj-1] != 0:
            idx = (i, newj)
            value = table[i+1, newj-1] + 2
            pr_que = pr_que.append(pd.Series([idx, value]), ignore_index=True)
            pr_que.drop(index=0, inplace=True)

        # find string with different start and end character
        elif string[i] != string[newj] and table[i, newj-1] != 0\
                and table[i+1, newj] != 0:

            idx = (i, newj)
            value = max(table[i, newj-1], table[i+1, newj])
            pr_que = pr_que.append(pd.Series([idx, value]), ignore_index=True)
            pr_que.drop(index=0, inplace=True)

        # if subsring can not be calculated yet, decrease priority
        else:
            pr_que.iloc[0, 1] -= 1

    # if subsring can not be calculated yet, decrease priority
    else:
        pr_que.iloc[0, 1] -= 1

    # make sure priority queue is ordered by priority
    pr_que = pr_que.sort_values(by=1, ascending=False).reset_index(drop=True)

print(f'The length of the longest palindromic substring is: {table[0,-1]}')
