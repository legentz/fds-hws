import numpy as np

class CompleteLinkage():
    def __init__(self, M, k):
        self.M = M  # point matrix
        self.m = M.shape[0]  # num points
        self.nclust = k  # num clusters
        self.clusters = {i : [i] for i in range(self.m)}
        self.D = dist(M, M)
        while len(self.clusters) > k:
            c1, c2 = self.findClosestClusters()
            self.merge(c1, c2)

    def distance(self, c1, c2):
        C1 = self.clusters[c1]
        C2 = self.clusters[c2]
        return max([self.D[i,j] for i in C1 for j in C2])

    def findClosestClusters(self):
        d = np.Inf
        closest = None
        for c1 in self.clusters:
            for c2 in self.clusters:
                if self.distance(c1, c2) < d and c1 != c2:
                    d = self.distance(c1, c2)
                    closest = (c1, c2)
        return closest

    def merge(self, c1, c2):
        self.clusters[c1] = self.clusters[c1] + self.clusters[c2]
        del self.clusters[c2]

def euc(x, y):
    return np.sqrt(np.sum((y-x)**2))

def dist(X, Y):
    # distance matrix of two sets of points
    D = np.zeros((X.shape[0], Y.shape[0]))
    for i in range(X.shape[0]):
        for j in range(Y.shape[0]):
            D[i, j] = euc(X[i], Y[j])
    return D
