from heapq import heapify, heappop, heappush 
num2letter = dict(zip(range(14), ' ABCDEFGHIJKLM'))


def dij(G, w, u):
    """G is a list of edges"""
    deletedNodes = set()
    stack = [(float('inf'), node) for node in range(len(G))]
    stack[u] = (0, u)
    dist = [float('inf') for node in range(len(G))]
    dist[u] = 0
    heapify(stack)
    while stack:
        du, u = heappop(stack)  # hm.. shouldn't this be a priority queue?
        while (du, u) in deletedNodes and stack != []:
            deletedNodes.remove((du, u))
            du, u = heappop(stack)
        for v in G[u]:
            if dist[v] > dist[u] + w[(u, v)]:
                dv = du + w[(u, v)]
                if (du, u) in deletedNodes:
                    deletedNodes.remove((du, u))  # no longer deleted
                else:
                    heappush(stack, (dv, v))  # push new change
                    # mark node as deleted
                    deletedNodes.add((dist[v], v))
                dist[v] = dv


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
w[(2, 3)] = 2
w[(2, 6)] = 6
w[(2, 7)] = 6
w[(3, 4)] = 1
w[(3, 7)] = 2
w[(4, 8)] = 4
w[(4, 7)] = 1
w[(5, 6)] = 5
w[(7, 6)] = 1
w[(7, 8)] = 1

dij(G, w, 1)
