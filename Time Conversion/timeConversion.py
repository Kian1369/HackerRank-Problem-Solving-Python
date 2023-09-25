#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Case I: s= "12:XX:XXAM"
    if (s[:2] == "12" and s[-2:]== "AM"):
        return "00" + s[2:-2]
    # Case II: s= "12:XX:XXPM"
    elif (s[:2] == "12" and s[-2:]== "PM"):
        return s[:-2]
    else:
        myString = s[2:-2]
        hour_Conversion = 12 + int(s[:2]) if s.endswith("PM") else int(s[:2])
        hour_Conversion = hour_Conversion % 24  # Handle edge case where hour_Conversion becomes 24
        return str(hour_Conversion).zfill(2) + myString
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
