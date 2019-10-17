"""

    Problem 6:

    The sum of the squares of the first ten natural numbers is,

    12 + 22 + ... + 102 = 385
    The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)2 = 552 = 3025
    Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""

import numpy as np
import time

if __name__ == "__main__":
    starting_time = time.time()

    print(sum(range(1,101,1))**2 - sum(np.square(range(1,101,1))))

    print("\nExecution time: ", float(time.time() - starting_time), " seconds")
