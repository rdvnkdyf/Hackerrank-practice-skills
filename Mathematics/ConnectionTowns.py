#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'connectingTowns' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY routes
#

def connectingTowns(n, routes):
    # This function calculates the total number of paths from the first
    # to the last town, given the number of routes between consecutive towns.
    # The result is returned modulo 1234567.

    # The modulo value as specified in the problem.
    MOD = 1234567
    
    # Initialize the total number of paths to 1. This acts as the starting
    # point for our product calculation.
    total_paths = 1
    
    # The total number of paths is the product of the number of routes
    # between each consecutive pair of towns. We iterate through the
    # 'routes' array, which contains n-1 elements representing the
    # routes from T_i to T_i+1.
    for num_routes in routes:
        # For each leg of the journey, we multiply the current total paths
        # by the number of routes for that leg.
        total_paths *= num_routes
        
        # To avoid integer overflow and meet the problem's requirement,
        # we apply the modulo operation after each multiplication.
        total_paths %= MOD
        
    return total_paths

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        routes = list(map(int, input().rstrip().split()))

        result = connectingTowns(n, routes)

        fptr.write(str(result) + '\n')

    fptr.close()
