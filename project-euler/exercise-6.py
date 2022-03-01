# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

base_list = list(range(1, 101))
square_of_sum = sum(base_list) ** 2
sum_of_squares = sum(map(lambda x: x * x, base_list))
answer = sum_of_squares - square_of_sum
print(abs(answer))
