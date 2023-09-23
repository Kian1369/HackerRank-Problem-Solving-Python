#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Creating an empty array to append the rounding grades and return at the end:
    arr = []
    for grade in grades:
        # Case 1: 
        if grade < 38:
            arr.append(grade)
          
        # Case 2: If the remainder of any number divided by 5 id 3, the number will be rounded to two numbers above:
        elif (grade % 5) == 3:
            arr.append(grade + 2)
          
        # Case 3: If the remainder of any number divided by 5 id 4, the number will be rounded to one numbers above:
        elif (grade % 5) == 4:
            arr.append(grade + 1)

      # Case 4: In any other case the grade won'y be rounded:
        else:
            arr.append(grade)
    return arr
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
