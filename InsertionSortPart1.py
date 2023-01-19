#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    
    for idx in range(n-1, 0, -1):
        value = arr[idx]
        
        while value < arr[idx-1] and idx > 0:
            arr[idx] = arr[idx-1]
            print(*arr)
            idx -= 1
            
        arr[idx] = value
        
    print(*arr)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
