#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'movingTiles' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER s1
#  3. INTEGER s2
#  4. INTEGER_ARRAY queries
#

def movingTiles(l, s1, s2, queries):
    """
    Given the side length of two squares, their velocities, and an array of queries
    (overlapping areas), this function computes the time at which the overlapping
    area is equal to each query value.

    Parameters:
    l (int): The side length of the two squares.
    s1 (int): The velocity of the first square.
    s2 (int): The velocity of the second square.
    queries (list): An array of query values, representing the overlapping area.

    Returns:
    list: An array of answers to the queries, in order, as floating-point values.
    """
    # Calculate the absolute difference in velocities
    delta_s = abs(s1 - s2)

    # Handle the special case where velocities are the same
    # The overlap area never changes in this case.
    if delta_s == 0:
        # If the query is the initial area, time can be anything, but we can't
        # determine a unique time. If the query is different, it's impossible.
        # Based on the problem constraints, this case might not occur with
        # different query values. We return 0.0 for a safe value.
        return [0.0] * len(queries)

    results = []
    for area_query in queries:
        # The new side length of the overlapping square is the square root of the area.
        # This will be in the range 0 <= sqrt(area) <= l.
        sqrt_area = math.sqrt(area_query)

        # The distance between the squares along the x-axis is (delta_s * t) / sqrt(2).
        # The new side length of the overlapping square is l - (delta_s * t) / sqrt(2).
        # So, sqrt(area) = l - (delta_s * t) / sqrt(2)
        # Solving for t, we get: t = (l - sqrt(area)) * sqrt(2) / delta_s
        time = (l - sqrt_area) * math.sqrt(2) / delta_s

        results.append(time)

    return results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    l = int(first_multiple_input[0])

    s1 = int(first_multiple_input[1])

    s2 = int(first_multiple_input[2])

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = movingTiles(l, s1, s2, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
