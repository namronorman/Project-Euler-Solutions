"""

    Problem 9:

    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a^2 + b^2 = c^2
    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.

"""

def find_special_pythagorean_triplet(number):
    for c in range(1, number + 1, 1):
        for b in range(1, number + 1, 1):
            for a in range(1, number + 1, 1):
                if a < b < c:
                    if a + b + c == number:
                        if a**2 + b**2 == c**2:
                            return (a * b * c)

    return -1


if __name__ == "__main__":
    print(find_special_pythagorean_triplet(1000))