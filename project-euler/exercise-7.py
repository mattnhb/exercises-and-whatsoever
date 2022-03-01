# By listing the first six prime numbers:
# 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?


def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_nth_prime(n):
    prime_amount = 0
    prime = 1

    while prime_amount < n:
        prime += 1
        if is_prime(prime):
            prime_amount += 1
    return prime


print(get_nth_prime(10001))
