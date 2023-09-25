#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Calculate the number of three-character substrings:
    codeLength = len(s)//3
    count = 0
    strSlice = []
    
    # Iterating through the string and extract three-character substrings
    for i in range(codeLength):
        start_index = i * 3
        end_index = start_index + 3
        substring = s[start_index:end_index]
        strSlice.append(substring)
    
    # Looping through each sub-string in our list and check if the string follows the "SOS" pattern. If not, add 1 to count variable:
    for subStr in strSlice:
        if subStr[0] != 'S':
            count+=1
        if subStr[1] != 'O':
            count+=1
        if subStr[2] != 'S':
            count+=1

    return count
    
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
