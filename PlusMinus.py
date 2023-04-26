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
    # Write your code here
    Positive, Negative, Zero = 0, 0, 0
    i = 0
    while i < n:
        
        #print(i, '=', arr[i])
        if arr[i] > 0:
            Positive += 1
        elif arr[i] < 0 :
            Negative += 1
        else:
             Zero += 1
        i += 1
    #print(Positive, Zero, Negative)
    P = Positive / n
    N = Negative / n
    Z = Zero / n
    print('{0:.6f}'.format(P))
    print('{0:.6f}'.format(N))
    print('{0:.6f}'.format(Z))
        
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
