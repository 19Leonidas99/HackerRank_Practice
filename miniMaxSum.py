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
    min, max = 0, 0
    n = 0
    i = 0
    arr.sort()
    #print(arr)
    while n < 4:
        min += arr[n]
        n += 1
        #print(n) 
    
    i = -1
    while i > -5:
        max += arr[i]
        i -= 1
        #print(i)
    
    print(min, max)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))
    #print(arr)

    miniMaxSum(arr)
