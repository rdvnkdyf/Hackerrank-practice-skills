#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gameWithCells' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def gameWithCells(n, m):
    """
    Calculates the minimum number of packages required to supply all bases
    in an n x m grid.

    Args:
        n (int): The number of rows in the grid.
        m (int): The number of columns in the grid.

    Returns:
        int: The minimum number of packages required.
    """
    # A single package can cover a 2x2 grid of cells.
    # To cover all 'n' rows, we need a certain number of rows of packages.
    # This can be found by dividing 'n' by 2 and rounding up, as a row of packages can supply two rows of cells.
    # The math.ceil() function is perfect for this.
    rows_needed = math.ceil(n / 2)
    
    # Similarly, to cover all 'm' columns, we need a certain number of columns of packages.
    columns_needed = math.ceil(m / 2)
    
    # The total number of packages is the product of the rows and columns of packages.
    return int(rows_needed * columns_needed)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = gameWithCells(n, m)

    fptr.write(str(result) + '\n')

    fptr.close()