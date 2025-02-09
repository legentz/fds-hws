import numpy as np
import time, sys
from functools import reduce

# faster method to calculate divisors of n
def get_divisors(n):    
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

# main function
def get_trasformation(input_):

	# shallow copy
	output_ = input_[::]

	# empty vector
	transition_ = np.zeros(len(input_), dtype=int)

	# looping backwards
	for i in range(len(input_), 0, -1):
		
		# skip already switched on bulbs
		if output_[i - 1] == 1: continue

		# add to transition vector
		transition_[i - 1] = 1

		# switch each bulb that's a divisor of i
		for d in get_divisors(i):

			# switch the state
			output_[d - 1] = 1 if output_[d - 1] == 0 else 0

	# print out through list expansion
	print(*transition_)

# main
if __name__ == '__main__':
	
	# process input
	input_ = np.loadtxt(sys.argv[1], dtype=int)

	# init
	get_trasformation(input_)