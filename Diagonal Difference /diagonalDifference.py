#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    primaryDiagonal = 0
    secondaryDiagonal = 0
  
    # Since we are dealing with a "square matrix" we could be iterating through the length of the first dimension of the array, 
    # and it does not matter which. So either arr[0], arr[1], ..., arr[i] is correct (I chose len(arr[0]):
    for i in range(len(arr[0])):
        primaryDiagonal += arr[i][i]
        secondaryDiagonal += arr[i][len(arr)-1-i]
    return abs(primaryDiagonal-secondaryDiagonal)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
