"""

    Problem 1:

    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.

"""

import time

def multiples_of(limit):
    multiples_sum = 0

    for i in range(1, limit):
        if i%3 == 0 or i%5 == 0:
            multiples_sum = multiples_sum + i

    print(multiples_sum)

if __name__ == "__main__":
    starting_time = time.time()

    multiples_of(limit = 1000)

    print("\nExecution time: ", float(time.time() - starting_time), " seconds")