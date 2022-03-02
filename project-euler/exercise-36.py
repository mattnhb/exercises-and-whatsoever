# The decimal number, 585 = 1001001001.2 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include leading zeros.)

decimal_palindromic_list = list(
    filter(lambda x: x == x[::-1], map(str, range(1, 1000000)))
)
both_palindromic_list = [
    int(decimal)
    for decimal in decimal_palindromic_list
    if bin(int(decimal)).replace("0b", "")
    == bin(int(decimal)).replace("0b", "")[::-1]
]
sum_of_both_palindromic = sum(both_palindromic_list)
print(sum_of_both_palindromic)