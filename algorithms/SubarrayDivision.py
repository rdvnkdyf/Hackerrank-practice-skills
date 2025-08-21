#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    """
    Determines how many ways a chocolate bar can be divided to match a birthday.

    Args:
        s (list): A list of integers on the chocolate squares.
        d (int): Ron's birth day.
        m (int): Ron's birth month.

    Returns:
        int: The number of ways the bar can be divided.
    """
    count = 0
    
    # Iterate through the list of squares, considering each possible starting point
    # for a segment of length m.
    # The loop should go up to len(s) - m + 1 to ensure that the segment
    # of length m does not go out of bounds.
    for i in range(len(s) - m + 1):
        # Create a contiguous segment of the chocolate bar of length m,
        # starting from index i.
        segment = s[i:i+m]
        
        # Check if the sum of the integers in the segment equals Ron's birth day.
        if sum(segment) == d:
            count += 1
            
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
