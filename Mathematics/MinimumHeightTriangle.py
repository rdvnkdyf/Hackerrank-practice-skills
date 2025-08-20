#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lowestTriangle' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER trianglebase
#  2. INTEGER area
#

def lowestTriangle(trianglebase, area):
    # The formula for the area of a triangle is: Area = (base * height) / 2.
    # To find the minimum height, we can rearrange the formula: height = (2 * Area) / base.
    # Since the area must be *at least* the given value, we need to find the smallest
    # integer height that satisfies the condition: (base * height) / 2 >= area.
    
    # Calculate the minimum height required to achieve the exact area.
    height_needed = (2 * area) / trianglebase
    
    # The height must be an integer, and since the area must be *at least* 'area',
    # we need to round up to the next whole number if the result is not an integer.
    # The math.ceil() function handles this for us.
    return math.ceil(height_needed)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    trianglebase = int(first_multiple_input[0])

    area = int(first_multiple_input[1])

    height = lowestTriangle(trianglebase, area)

    fptr.write(str(height) + '\n')

    fptr.close()