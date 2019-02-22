#include "pch.h"
#include <iostream>

int main()
{
	/*
	
	Problem 2 
	Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

	1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

	By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

	*/

	unsigned long int f_current = 1, f_previous = 1, f_max = 4000000, f_sum = 0;

	while (true) {
		// Grab a snapshot of the current sequence.
		unsigned long int t = f_current;

		// Up the current sequence
		if (f_current + f_previous <= f_max) {
			f_current = f_current + f_previous;

			// Increase the sum if the current sequence is an even number.
			if (f_current % 2 == 0)
				f_sum = f_sum + f_current;
		} else {
			// If the next sequence is greater than the max requested, break the loop.
			break;
		}

		// Set the previous value to the snapshot value
		f_previous = t;
	}

	std::cout << f_sum;

	return 0;
}