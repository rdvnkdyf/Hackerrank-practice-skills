#!/bin/python3

import math
import os
import random
import re
import sys
import collections
#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    
    
    
    counts = collections.Counter(arr)
    
    
    max_frequency = max(counts.values())
    
    
    most_frequent_birds = []
    for bird_id, frequency in counts.items():
        if frequency == max_frequency:
            most_frequent_birds.append(bird_id)
            
    
    return min(most_frequent_birds)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()