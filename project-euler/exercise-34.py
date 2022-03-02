# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# Note: As 1! = 1 and 2! = 2 are not sums they are not included.
import math


total = 0
factorials = {str(number): math.factorial(number) for number in range(10)}

for number in range(3, 999999):
    factorial_sum = 0
    for sub_number in str(number):
        factorial_sum += factorials[sub_number]
    if factorial_sum == number:
        total += factorial_sum

print(total)
