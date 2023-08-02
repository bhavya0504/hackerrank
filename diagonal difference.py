# Diagonal Difference.

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
    # Write your code here
    li = [0,0]
    l = len(arr[0])
    a = [arr[i][i] for i in range(l)]              
    b = [arr[l-1-i][i] for i in range(l-1,-1,-1)]  
    for j in range(l):
        li[0]+=a[j]
        li[1]+=b[j]
    return abs(li[0]-li[1])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
