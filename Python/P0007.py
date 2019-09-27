"""

    Problem 7:

    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

    What is the 10 001st prime number?

"""

import math

def is_prime(number):
    if number%2 == 0 and number > 2 or number == 1:
        return False

    return all(number%i for i in range(3, int(math.sqrt(number)) + 1, 2))

if __name__ == "__main__":
    digit = 0
    prime_count = 0

    while prime_count < 10001:
        digit = digit + 1

        if is_prime(digit):
            prime_count = prime_count + 1

    print(digit)