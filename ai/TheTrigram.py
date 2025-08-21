#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

if __name__ == '__main__':
    # Read the entire input text. In many online judges,
    # 'sys.stdin.read()' is a common way to handle large, multi-line input.
    # We'll use a simple input() call as per the template and assume it reads
    # the entire text chunk.
    s = sys.stdin.read()

    # Convert the entire text to lowercase for case-insensitivity.
    s = s.lower()

    # Split the text into sentences using the period as a delimiter.
    # This ensures that trigrams do not cross sentence boundaries.
    sentences = s.split('.')

    # Dictionaries to store trigram counts and the order of their first appearance.
    trigram_counts = Counter()
    trigram_order = []

    # Iterate through each sentence to find trigrams.
    for sentence in sentences:
        # Strip leading/trailing whitespace and split the sentence into words.
        words = sentence.strip().split()
        
        # Check if there are at least 3 words to form a trigram.
        if len(words) >= 3:
            # Iterate through the words to form all possible trigrams.
            for i in range(len(words) - 2):
                # Join three consecutive words to form a trigram string.
                trigram = " ".join(words[i:i+3])
                
                # If this is the first time we've seen this trigram,
                # add it to our ordered list.
                if trigram not in trigram_counts:
                    trigram_order.append(trigram)
                
                # Increment the count for the trigram.
                trigram_counts[trigram] += 1

    # Find the most frequent trigram, with the tie-breaker rule.
    max_freq = 0
    result = ""

    # Iterate through the trigrams in the order they first appeared.
    for trigram in trigram_order:
        # Get the frequency of the current trigram.
        current_freq = trigram_counts[trigram]
        
        # If the current frequency is greater than the max frequency found so far,
        # update the max frequency and the result. This approach naturally handles
        # the tie-breaker rule because the first trigram encountered with the
        # highest frequency will be stored.
        if current_freq > max_freq:
            max_freq = current_freq
            result = trigram
            
    # Print the most frequent trigram.
    print(result)