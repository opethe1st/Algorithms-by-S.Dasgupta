
def BellmanFord(G, w, start):
    """G is an adjacency list representation of a Graph G"""
    n = len(G)
    visited = [False]*n
    dist = [float('inf')]*n
    dist[start] = 0
    for _ in range(n):
        visited = [False]*n
        print _, dist
        for e in w:
            u, v = e
            if dist[v] > dist[u]+w[(u, v)]:
                    dist[v] = dist[u]+w[(u, v)]


G = [[] for i in xrange(10)]
G[0] = [1, 3, 5, 6]
G[1] = [2, 3]
G[2] = [7, 8]
G[3] = [4, 6]
G[5] = [6, 8]
G[6] = [4]
G[7] = [9]
G[8] = [7]
G[9] = [8]
w = {}
w[(1, 2)] = 4
w[(1, 3)] = -2
w[(2, 7)] = -2
w[(2, 8)] = -4
w[(3, 4)] = 2
w[(3, 6)] = 1
w[(5, 8)] = 3
w[(5, 6)] = -2
w[(6, 4)] = 3
w[(7, 9)] = -1
w[(8, 7)] = 1
w[(9, 8)] = 1
w[(0, 1)] = 7
w[(0, 2)] = 6
w[(0, 6)] = 5
w[(0, 5)] = 6
BellmanFord(G, w, 0)

