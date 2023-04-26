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
    # Write your code here
    x = s.split(':')
    cv = ''
    #print(x)
    if x[0] == '12' and 'A' in x[2]:
        for c in x[2]:
            if c.isdigit():
                cv += c
        
        print('00:' + x[1] + ':' + cv)
            
    
    elif x[0] == '12' and 'P' in x[2]:
        for c in x[2]:
            if c.isdigit():
                cv += c
        
        print(x[0] + ':' + x[1] + ':' + cv)
        
    elif 'A' in x[2]:
        for c in x[2]:
            if c.isdigit():
                cv += c
        
        print(x[0] + ':' + x[1] + ':' + cv)
    
    else:
        for c in x[2]:
            if c.isdigit():
                cv += c
        #print(type(x[0]))
        cv2 = int(x[0]) + 12
        #print(type(cv2),cv2)
        
        print(str(cv2) + ':' + x[1] + ':' + cv)
        

if __name__ == '__main__':
    

    s = input()

    result = timeConversion(s)
    

    