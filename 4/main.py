import sys
import numpy as np 
from libdescent import GradientDescent

# check argv input size
assert len(sys.argv) > 2, 'Missing required X, Y txt(s)'

# input
X = np.loadtxt(sys.argv[1])
Y = np.loadtxt(sys.argv[2])

# init
gd = GradientDescent(X, Y)

# run and pretty print
print(' '.join("{:.02f}".format(x) for x in gd.run()))