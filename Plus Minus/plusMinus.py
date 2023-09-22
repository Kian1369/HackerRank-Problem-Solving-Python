#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos_count=0
    neg_count=0
    zero_count=0
    for i in range(len(arr)):
        if arr[i] > 0:
            pos_count = pos_count + 1
        elif arr[i] < 0:
            neg_count = neg_count + 1 
        else:
            zero_count = zero_count +1
    print(round(pos_count/len(arr),6))
    print(round(neg_count/len(arr),6))
    print(round(zero_count/len(arr),6))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
