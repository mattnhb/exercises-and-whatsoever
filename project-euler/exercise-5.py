# 2520 is the smallest number that can be divided by each of the
# numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible
# by all of the numbers from 1 to 20?

divisor_list = [19, 17, 16, 13, 11]


def divisible(n, lst):
    return all(map(lambda y: n % y == 0, lst))


def get_smallest_number():
    n = 2520
    while not divisible(n, divisor_list):
        n += 2520
    return n


answer = get_smallest_number()
print(answer)
