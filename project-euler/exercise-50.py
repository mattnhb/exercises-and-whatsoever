# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13

# This is the longest sum of consecutive primes that adds to a prime below one-hundred.

# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

# Which prime, below one-million, can be written as the sum of the most consecutive primes?
from typing import List


def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_prime_list() -> List[int]:
    return [n for n in range(2, 1000000) if is_prime(n)]


lista = get_prime_list()
lastj = len(lista)
lenght = 0
largest = 0
for i in range(len(lista)):
    for j in range(i + lenght, lastj):
        soma = sum(lista[i:j])
        if soma < 1000000:
            if soma in lista:
                lenght = j - i
                largest = soma
        else:
            lastj = j + 1
            break

print(largest)