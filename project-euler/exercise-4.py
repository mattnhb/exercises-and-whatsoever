# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

list1 = list(range(100, 999))

list2 = list(range(100, 999))

products = [num1 * num2 for num1 in list1 for num2 in list2]

largest_palindrome = max(filter(lambda x: x == x[::-1], map(str, products)), key=int)

print(largest_palindrome)
