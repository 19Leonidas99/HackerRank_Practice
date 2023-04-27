#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    L1, L2, L3 = [], [], []
    print(a)
    if len(a) == 1:
        print(int(a[0]))
    for i in a:
        if i not in L1:
            L1.append(i)
        else:
            L2.append(i)

    for j in L1:
        if j not in L2:
            L3.append(j)
    return(int(L3[0]))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
