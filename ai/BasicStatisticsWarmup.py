import math
import statistics
from collections import Counter

# Read the number of integers
try:
    N = int(input())
except (ValueError, IndexError):
    print("Invalid input for the number of integers.")
    exit()

# Read the space-separated integers
try:
    numbers = [int(num) for num in input().split()]
except (ValueError, IndexError):
    print("Invalid input for the list of integers.")
    exit()

# Sanity check: Ensure the number of integers read matches N
if len(numbers) != N:
    N = len(numbers)

# Calculate Mean
mean = statistics.mean(numbers)
print(f"{mean:.1f}")

# Calculate Median
numbers.sort()
median = statistics.median(numbers)
print(f"{median:.1f}")

# Calculate Mode(s) - handling multiple modes by taking the smallest
try:
    mode = statistics.mode(numbers)
    print(mode)
except statistics.StatisticsError:
    counts = Counter(numbers)
    max_count = max(counts.values())
    modes = [k for k, v in counts.items() if v == max_count]
    print(min(modes))

# Calculate Standard Deviation (using population formula)
stdev = statistics.pstdev(numbers)
print(f"{stdev:.1f}")

# Calculate Confidence Interval
# Formula: mean +/- (Z-score * (Standard Deviation / sqrt(N)))
# Z-score for 95% confidence interval is given as 1.96
standard_error = stdev / math.sqrt(N)
lower_bound = mean - 1.96 * standard_error
upper_bound = mean + 1.96 * standard_error
print(f"{lower_bound:.1f} {upper_bound:.1f}")