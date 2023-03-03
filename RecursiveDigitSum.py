#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def calcSuper(n):
    if n <= 9:
        return n
    
    ans = n%10 + calcSuper(n//10)
    
    return ans

def superDigit(n, k):
    # Write your code here
    ans = list(n)
    total = 0

    for elm in ans:
        total += (int(elm))
            
    ans = total*k
    
    while ans >= 10:
        ans = calcSuper(ans)
    
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
