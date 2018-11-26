import numpy as np
import random

# m denotes the number of examples here, not the number of features
def gradientDescent(x, y, theta, alpha, m, numIterations):
    xTrans = x.transpose()
    for i in range(0, numIterations):
        print(x.shape, theta.shape)
        hypothesis = np.dot(x, theta)
        print(hypothesis.shape)
        loss = hypothesis - y
        print(loss.shape)
        # avg cost per example (the 2 in 2*m doesn't really matter here.
        # But to be consistent with the gradient, I include it)
        cost = np.sum(loss ** 2) / (2 * m)
        print("Iteration %d | Cost: %f" % (i, cost))
        # avg gradient per example
        gradient = np.dot(xTrans, loss) / m
        # update
        theta = theta - alpha * gradient
    return theta


def genData(numPoints, bias, variance, nfeature=2):
    x = np.zeros(shape=(numPoints, nfeature))
    y = np.zeros(shape=numPoints)
    # basically a straight line
    for i in range(0, numPoints):
        for j in range(0, nfeature):
            # bias feature
            x[i][j] = 1 if j == 0 else i
            # x[i][1] = i
            # our target variable
            y[i] = (i + bias) + random.uniform(0, 1) * variance
    return x, y

# gen 100 points with a bias of 25 and 10 variance as a bit of noise
x, y = genData(10000, 25, 10, 4)
print(x.shape)
print(y.shape)
# import sys; sys.exit(1)
np.savetxt('X1_t3.txt', x, delimiter=' ')
np.savetxt('Y1_t3.txt', y, delimiter=' ')

# print(x.shape, y.shape)
# print(x, y)
# x, y = np.loadtxt('X1.txt'), np.loadtxt('Y1.txt')

m, n = np.shape(x)
numIterations= 100000
alpha = 1 # 0.0005
theta = np.zeros(n)
theta = gradientDescent(x, y, theta, alpha, m, numIterations)
print(theta)