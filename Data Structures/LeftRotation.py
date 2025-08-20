#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def rotateLeft(d, arr):
    """
    Rotates an array 'arr' to the left by 'd' steps.

    Args:
        d (int): The number of left rotations.
        arr (list): The array to rotate.

    Returns:
        list: The rotated array.
    """
    n = len(arr)
    # The effective number of rotations is d modulo n
    d = d % n
    
    # Slice the array from the d-th element to the end,
    # and then concatenate it with the slice from the beginning to the d-th element.
    rotated_arr = arr[d:] + arr[:d]
    
    return rotated_arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
