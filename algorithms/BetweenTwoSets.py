#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
def gcd(a, b):
    
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    
    return (a * b) // gcd(a, b)
    
def getTotalX(a, b):
    
    
    lcm_of_a = a[0]
    for i in range(1, len(a)):
        lcm_of_a = lcm(lcm_of_a, a[i])
    
    
    gcd_of_b = b[0]
    for i in range(1, len(b)):
        gcd_of_b = gcd(gcd_of_b, b[i])
        
    count = 0
    
    
    current_multiple = lcm_of_a
    while current_multiple <= gcd_of_b:
        
        if gcd_of_b % current_multiple == 0:
            count += 1
        
        current_multiple += lcm_of_a
        
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()