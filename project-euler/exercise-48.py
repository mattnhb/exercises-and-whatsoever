# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.


def get_self_power(num) -> int:
    return num ** num


def get_sum_of_powers() -> int:
    return sum(get_self_power(num) for num in range(1, 1001))


def get_last_ten_digits() -> str:
    return str(get_sum_of_powers())[-10:]


print(get_last_ten_digits())
