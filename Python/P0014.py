"""

    Problem 14:

    The following iterative sequence is defined for the set of positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million.

"""

import time

def collatz(n):
    terms = 1

    while n != 1:
        terms = terms + 1

        if n%2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1

    return terms
        

if __name__ == "__main__":
    starting_time = time.time()
    
    longest_chain = 0
    biggest_number = 0

    for i in range(2, 1000000, 1):
        c = collatz(i)

        if c >= longest_chain:
            longest_chain = c
            biggest_number = i

    print(biggest_number)

    print("\nExecution time: ", float(time.time() - starting_time), " seconds")