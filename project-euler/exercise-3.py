# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

from math import sqrt


def get_largest_prime_factor(number=600851475143) -> int:
    sqrt_number = sqrt(number)
    x = 2
    while x <= sqrt_number:
        if number % x == 0:
            number /= x
            sqrt_number = sqrt(number)
        else:
            x += 1
    answer = number
    return answer


answer = get_largest_prime_factor()
print(answer)
