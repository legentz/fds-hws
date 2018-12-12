import numpy as np
import time
import sys
from functools import reduce

def timeit(method):
    def timed(*args, **kw):
        ts = time.perf_counter()
        result = method(*args, **kw)
        te = time.perf_counter()
        print('%r  %2.10f s' % (method.__name__, (te - ts)))
        return result
    return timed

def factors(n):    
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def get_divisors(i):
	return [x for x in range(1, i + 1) if i % x == 0]

@timeit
def get_trasformation(input_):
	output_ = input_[::]
	transition_ = np.zeros(len(input_), dtype=int)

	# looping backwards
	for i in range(len(input_), 0, -1):
		
		# skip already switched on bulbs
		if output_[i - 1] == 1: continue

		# add to transition vector
		transition_[i - 1] = 1

		# switch each bulb
		for d in factors(i):
			output_[d - 1] = 1 if output_[d - 1] == 0 else 0

	print(*transition_)


if __name__ == '__main__':
	
	# process input
	input_ = np.loadtxt(sys.argv[1], dtype=int)

	# init
	get_trasformation(input_)