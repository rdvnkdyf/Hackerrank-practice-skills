#!/bin/python3

import math
import os
import random
import re
import sys

def get_digit_sum(num):
    """
    Calculates the sum of the digits of a number.
    """
    digit_sum = 0
    # Use a while loop to extract and sum each digit
    while num > 0:
        digit_sum += num % 10
        num //= 10
    return digit_sum

if __name__ == '__main__':
    n = int(input().strip())
    
    # Initialize the best divisor and its digit sum.
    # We can start with 1, as it's a divisor for all positive integers.
    best_divisor = 1
    max_digit_sum = get_digit_sum(1)
    
    # Iterate through all numbers from 1 up to n to find divisors
    for i in range(1, n + 1):
        if n % i == 0:
            # 'i' is a divisor of n. Now check if it's the "best" one.
            current_digit_sum = get_digit_sum(i)
            
            # Rule 1: A larger digit sum is better.
            if current_digit_sum > max_digit_sum:
                max_digit_sum = current_digit_sum
                best_divisor = i
            
            # Rule 2: If the digit sums are equal, the smaller number is better.
            # Since we are iterating from 1 to n, the first divisor we find
            # with a particular digit sum will be the smallest.
            # So, we don't need to update if the digit sums are equal.
            # Our 'best_divisor' will already be the correct one.
    
    print(best_divisor)