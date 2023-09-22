#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#

def matchingStrings(strings, queries):
    # Creating an empty list to store the frequency of occurrence of each query string in strings:
    result= []

    # So for each element in the queries list we will iterate through the strings list and if the same element is found we increment the variable count:
    # Important Note: Each time we go over all elements in the strings list for a single element in the queries list, we need to set the variable count=0
    for i in range(len(queries)):
        count=0
        for j in range(len(strings)):
            if queries[i] == strings[j]:
                count+=1
            else:
                count
        result.append(count)
      
    # Returning the result array
    return result 


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
