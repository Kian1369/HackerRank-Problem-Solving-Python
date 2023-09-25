#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    result = []
    minScore = scores[0]
    maxScore = minScore
    max_Record_Count = 0
    min_Record_Count = 0 
    for i in range(len(scores)-1):
        if scores[i+1] < minScore:
            minScore = scores[i+1]
            min_Record_Count = min_Record_Count +1
        elif scores[i+1] > maxScore:
            maxScore = scores[i+1]
            max_Record_Count = max_Record_Count +1
        else:
            minScore = minScore
            maxScore = maxScore
    result.append(max_Record_Count)
    result.append(min_Record_Count)
    return result
            
                
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
