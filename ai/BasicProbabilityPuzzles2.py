import math

# Calculate the total number of possible outcomes for two 6-sided dice.
total_outcomes = 6 * 6

# Count the number of favorable outcomes.
# Favorable outcomes are when the dice values are different and their sum is 6.
favorable_outcomes = 0
for die1 in range(1, 7):
    for die2 in range(1, 7):
        if die1 != die2 and die1 + die2 == 6:
            favorable_outcomes += 1

# Find the greatest common divisor (GCD) to simplify the fraction.
gcd = math.gcd(favorable_outcomes, total_outcomes)

# Calculate the numerator and denominator of the irreducible fraction.
numerator = favorable_outcomes // gcd
denominator = total_outcomes // gcd

# Print the result in the required "numerator/denominator" format.
print(f"{numerator}/{denominator}")