#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a DOUBLE.
# The function accepts 2D_INTEGER_ARRAY coordinates as parameter.
#

def solve(coordinates):
    x_coords = []
    y_coords = []
    
    for x, y in coordinates:
        if y == 0:
            x_coords.append(x)
        else:
            y_coords.append(y)
            
    max_dist_squared = 0
    
    if x_coords:
        max_dist_squared = max((max(x_coords) - min(x_coords))**2, max_dist_squared)
        
    if y_coords:
        max_dist_squared = max((max(y_coords) - min(y_coords))**2, max_dist_squared)
        
    if x_coords and y_coords:
        max_x = max(x_coords)
        min_x = min(x_coords)
        max_y = max(y_coords)
        min_y = min(y_coords)

        max_dist_squared = max(
            min_x**2 + min_y**2,
            min_x**2 + max_y**2,
            max_x**2 + min_y**2,
            max_x**2 + max_y**2,
            max_dist_squared
        )
    
    return math.sqrt(max_dist_squared)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    coordinates = []

    for _ in range(n):
        coordinates.append(list(map(int, input().rstrip().split())))

    result = solve(coordinates)

    fptr.write(str(result) + '\n')

    fptr.close()
