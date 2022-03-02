# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!
def get_factorial(number) -> int:
    if number == 1:
        return 1
    else: 
        return get_factorial(number - 1) * number

factorial_100 = get_factorial(100)
answer = sum([int(element) for element in str(factorial_100)])
print(answer)