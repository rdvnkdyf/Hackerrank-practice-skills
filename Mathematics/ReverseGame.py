#!/bin/python3

import sys

def solve():
    t_str = sys.stdin.readline().strip()
    if not t_str:
        return
    t = int(t_str)

    for _ in range(t):
        try:
            first_multiple_input = sys.stdin.readline().rstrip().split()
            if not first_multiple_input:
                continue

            n = int(first_multiple_input[0])
            k = int(first_multiple_input[1])

            # The problem can be solved by simulating the reversals
            # and tracking the position of the ball with value k.
            
            # Initial position of the ball with value k is k.
            pos_k = k
            
            # The first reversal is from index 0 to N-1
            # A value at index i moves to (N-1)-i
            pos_k = (n - 1) - pos_k
            
            # Subsequent reversals from index 1 to N-1
            # We only care about the reversals that affect our ball.
            for i in range(1, n):
                # The reversal is on the sub-array from index i to N-1.
                # If our ball is in this sub-array, its position changes.
                if pos_k >= i:
                    # Let the length of the sub-array be L = (N-1) - i + 1.
                    # The new position will be relative to the start of the sub-array.
                    # A position p in the sub-array [i, N-1] moves to i + (N-1-p)
                    pos_k = i + (n - 1 - pos_k)
            
            print(pos_k)

        except (IOError, ValueError):
            continue

if __name__ == '__main__':
    solve()