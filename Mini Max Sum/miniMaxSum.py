#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    minSum = 0
    maxSum = 0
  
    # Sorting the array in order to get the position of min and max element:
    arr.sort()
    
    for i in range(1, len(arr)):
        maxSum = maxSum + arr[i]
    for j in range(0, len(arr)-1):
        minSum = minSum + arr[j]
    print(minSum, maxSum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
