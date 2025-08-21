#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'primeCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def primeCount(n):
    
    primes = []
    num = 2
    
    # Asal sayıları bulmak için basit bir algoritma
    while True:
        is_prime = True
        # Bir sayının asal olup olmadığını kontrol et
        for prime in primes:
            if prime * prime > num:
                break
            if num % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        
        # En son bulunan asal sayıyla çarpımı kontrol et
        if num == primes[-1]:
            product = 1
            count = 0
            for p in primes:
                if product * p > n:
                    # n'i aştı, bu son asal sayıyı sayma
                    return count
                product *= p
                count += 1
        
        num += 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = primeCount(n)

        fptr.write(str(result) + '\n')

    fptr.close()
