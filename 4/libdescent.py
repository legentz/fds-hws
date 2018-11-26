import numpy as np

class GradientDescent:

	def residual(Theta, X, Y):
		'''The vector of residual errors'''
		return Y - np.dot(X, Theta)

	def sse(Theta, X, Y):
		'''The SSE'''
		return np.sum(GradientDescent.residual(Theta, X, Y)**2)

	def gradient(Theta, X, Y):
		'''Gradient of the squared error at the given point'''
		return 2 * np.dot((np.dot(X, Theta) - Y), X)

	def __init__(self, X, Y):
		self.X = X
		self.Y = Y
		self.m, self.n = np.shape(X)

	def run(self, max_steps=100):
		'''Gradient descent'''
		Theta = np.zeros(self.n)
		sse = GradientDescent.sse(Theta, self.X, self.Y)
		alpha = 1
		for s in range(max_steps):
			g = GradientDescent.gradient(Theta, self.X, self.Y)
			newTheta = Theta - alpha * g
			newSse = GradientDescent.sse(newTheta, self.X, self.Y)
			if newSse < sse:
				Theta, sse = newTheta, newSse
				alpha *= 2
			else:
				alpha /= 2
		return Theta




