# Min Max sum.

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
    # Write your code here
    arr.sort()
    arr1=arr[0:len(arr)-1]
    arr2=arr[1::]
    sum1 = 0
    sum2 = 0
    for i in arr1:
        sum1=sum1+i
    for j in arr2:
        sum2 = sum2+j
    print(sum1,sum2)
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
