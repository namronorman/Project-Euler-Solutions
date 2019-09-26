"""

    Problem 4:

    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.

"""

import math

def num_digits(number):
    return int(math.log10(number)) + 1

def is_palindrome(number):
    # Exclude numbers that can't be mirrored due to an odd number of digits.
    if num_digits(number)%2 == 1:
        return False

    left = str(number)[:int(num_digits(number) / 2)]
    right = str(number)[-int(num_digits(number) / 2):]

    # Reverse right
    right = right[::-1]

    if left == right:
        return True

    return False

def biggest_palindrome(number_of_digits):
    biggest_palindrome = 0
    product = 0

    for x in range(1, 10**number_of_digits, 1):
        for y in range(1,10**number_of_digits, 1):
            product = x * y

            if is_palindrome(product) and product > biggest_palindrome:
                biggest_palindrome = product

    return biggest_palindrome


if __name__ == "__main__":
    print(biggest_palindrome(number_of_digits = 3))