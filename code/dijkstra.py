from heapq import heapq
num2letter = dict(zip(range(14), ' ABCDEFGHIJKLM'))


def dij(G, w, u):
    """G is a list of edges"""
    deletedNodes = set()
    A = [(float('inf'), node) for node in len(G)]
    A[u] = (0, u)
    dist = [float('inf') for node in len(G)]
    dist[u] = 0
    stack = heapify(A)
    while stack:
        du, u = stack.heappop(0)  # hm.. shouldn't this be a priority queue?
        while (du, u) in deletedNodes:
            deletedNodes.remove((du, u))
            du, u = stack.heappop(0)
        for v in G[u]:
            if dist[v] > dist[u] + w[(u, v)]:
                dv = du + w[(u, v)]
                dist[v] = dv
                if (du, u) in deletedNodes:
                    deletedNodes.remove((du, u))  # no longer deleted
                else:
                    stack.heappush((dv, v))  # push new change
                    # mark node as deleted
                    deletedNodes.add((dv, v))


G = [[] for i in xrange(9)]
G[1] = [2, 5, 6]
G[2] = [3, 6, 7]
G[3] = [4, 7]
G[4] = [7, 8]
G[5] = [6]
G[7] = [6, 8]
w = {}
w[(1, 2)] = 1
w[(1, 5)] = 4
w[(1, 6)] = 8
