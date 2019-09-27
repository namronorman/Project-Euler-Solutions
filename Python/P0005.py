"""

    Problem 5:

    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""

def divisible_by_list(list_of_numbers, number):
    return all((number/i)%1 == 0 for i in list_of_numbers)

if __name__ == "__main__":
    iteration = 1

    while divisible_by_list(list_of_numbers = range(1,21,1), number = iteration) == False:
        iteration = iteration + 1

    print(iteration)