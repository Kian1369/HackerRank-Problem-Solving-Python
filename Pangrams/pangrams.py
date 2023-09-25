#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
  
    # Making a list containing all English alphabets: (Not that we could've alternatively done sth like: alphabet = 'abcdefghijklmnopqrstuvwxyz'
    myList = [chr(item) for item in range(ord("a"), ord("z") + 1)]
    s = s.lower()
    # Looping through myList (each English letters) to see if they exist in the string passed to our function
    for i in range(len(myList)):
        if myList[i] in s:
            i += 1
        else:
            return "not pangram"
    return "pangram"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
