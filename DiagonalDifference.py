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
    firtstD, secondD = 0, 0
    i = 0
    j = -1
    while i < n:
        #print(i, arr[i][i])
        firtstD += int(arr[i][i])
        #print(i, j, arr[i][j])
        secondD += arr[i][j]
        i += 1
        j -= 1
    
    print(abs(firtstD - secondD))

if __name__ == '__main__':
    

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
        
    result = diagonalDifference(arr)
