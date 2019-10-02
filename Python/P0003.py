"""

    Problem 3:

    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?

"""

import math
import time

def is_prime(number):
    if number%2 == 0 and number > 2 or number == 1:
        return False

    return all(number%i for i in range(3, int(math.sqrt(number)) + 1, 2))

def largest_prime_factor(number):
    biggest_factor = 2

    for i in range(2, int(math.sqrt(number)), 1):
        if is_prime(number = i):
            if (number / i)%1 == 0:
                biggest_factor = i

    return biggest_factor

if __name__ == "__main__":
    starting_time = time.time()

    print(largest_prime_factor(number = 600851475143))

    print("\nExecution time: ", float(time.time() - starting_time), " seconds")