#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    """
    Calculates if Anna was charged correctly for her portion of the meal
    and prints the result.

    Args:
        bill: A list of integers representing the cost of each item.
        k: The zero-based index of the item Anna did not eat.
        b: The amount of money Anna contributed to the bill.
    """
    # Calculate the sum of all items on the bill.
    total_bill_sum = sum(bill)
    
    # Subtract the cost of the item Anna didn't eat to find the
    # total shared cost.
    shared_bill_sum = total_bill_sum - bill[k]
    
    # Calculate Anna's fair share, which is half of the shared bill.
    anna_fair_share = shared_bill_sum // 2
    
    # Check if Brian overcharged Anna.
    if b == anna_fair_share:
        # If the amount Anna paid is exactly her fair share, print "Bon Appetit".
        print("Bon Appetit")
    else:
        # If she was overcharged, calculate the difference and print it.
        amount_to_refund = b - anna_fair_share
        print(amount_to_refund)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
