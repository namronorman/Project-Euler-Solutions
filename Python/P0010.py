"""

    Problem 10:

    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.

"""

import math

def is_prime(number):
    if number%2 == 0 and number > 2 or number == 1:
        return False

    return all(number%i for i in range(3, int(math.sqrt(number)) + 1, 2))

if __name__ == "__main__":
    sum_of_primes = 0

    for i in range(1, 2000000, 1):
        if is_prime(i):
            sum_of_primes = sum_of_primes + i

    print(sum_of_primes)