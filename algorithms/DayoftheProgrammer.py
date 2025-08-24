#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    """
    Calculates the date of the 256th day of the year in Russia,
    considering the Julian and Gregorian calendar systems.

    Args:
        year: An integer representing the year.

    Returns:
        A string representing the date in the format 'dd.mm.yyyy'.
    """

    # Check the year to determine the correct calendar system and leap year rules.
    # The transition from Julian to Gregorian happened in 1918.

    # Julian calendar (1700-1917 inclusive)
    if year < 1918:
        # A Julian leap year is one that is divisible by 4.
        is_leap = (year % 4 == 0)
        
        # In a common year, Day of the Programmer is Sept 13 (31+28+31+30+31+30+31+31 = 243 days).
        # In a leap year, it's Sept 12 (31+29+31+30+31+30+31+31 = 244 days).
        if is_leap:
            return f"12.09.{year}"
        else:
            return f"13.09.{year}"

    # Transition year (1918)
    elif year == 1918:
        # In 1918, 13 days were skipped, so the 256th day comes earlier.
        # Common year days up to August = 243.
        # Subtract the 13 skipped days from the total.
        # 256 - (243 - 13) = 256 - 230 = 26.
        # The date is September 26th.
        return f"26.09.{year}"

    # Gregorian calendar (1919-2700 inclusive)
    else:
        # A Gregorian leap year is either divisible by 400,
        # or divisible by 4 but not by 100.
        is_leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
        
        # The days of the first 8 months are the same as the Julian calendar
        # but with the Gregorian leap year calculation.
        if is_leap:
            return f"12.09.{year}"
        else:
            return f"13.09.{year}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
