#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    """
    Calculates the number of times Maria breaks her season records for most and least points.

    Args:
        scores: A list of integers representing points scored per game.

    Returns:
        A list of two integers: [most_record_breaks, least_record_breaks].
    """
    if not scores:
        return [0, 0]

    # The first game establishes the initial records.
    min_record = scores[0]
    max_record = scores[0]

    # Initialize counters for record breaks.
    min_breaks = 0
    max_breaks = 0

    # Iterate through the scores starting from the second game.
    for score in scores[1:]:
        # Check if the current score breaks the maximum record.
        if score > max_record:
            max_record = score
            max_breaks += 1
        # Check if the current score breaks the minimum record.
        elif score < min_record:
            min_record = score
            min_breaks += 1

    return [max_breaks, min_breaks]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()