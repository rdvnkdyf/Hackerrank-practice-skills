#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'restaurant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER b
#

def restaurant(l, b):
    max_side_length = math.gcd(l, b)
    num_squares = (l // max_side_length) * (b // max_side_length)
    return num_squares

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        l = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = restaurant(l, b)

        fptr.write(str(result) + '\n')

    fptr.close()