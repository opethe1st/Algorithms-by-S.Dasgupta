from heapq import heapify, heappop, heappush


def primsAlgo(G, u, n):
    """G is a list of weighted edges, returns the minimum spanning tree"""
    deletedNodes = set()
    dist = [float('inf') for node in range(n+1)]
    dist[u] = 0
    heapify(G)
    w = {}
    for d, u, v in G:
        w[(u, v)] = d
    # print w
    # print G
    nodes = set()
    minSpanTree = []
    stack = G
    nG = [[] for i in xrange(9)]
    for d, u, v in G:
        nG[u].append(v)
    while len(nodes) != n:
        du, u, v = heappop(stack)
        # need to check if the node is in the minspantree already
        if u not in nodes or v not in nodes:
            minSpanTree.append((du, u, v))
            dist[u] = du
            nodes.add(u)
            nodes.add(v)
        while (du, u, v) in deletedNodes and stack != []:
            deletedNodes.remove((du, u, v))
            du, u, v = heappop(stack)
        for v in nG[u]:
            if dist[v] > dist[u] + w[(u, v)]:
                dv = du + w[(u, v)]
                if (du, u) in deletedNodes:
                    deletedNodes.remove((du, u))  # no longer deleted
                else:
                    heappush(stack, (dv, u, v))  # push new change
                    # mark node as deleted
                    deletedNodes.add((dist[v], v))
                dist[v] = dv
        print dist
    return minSpanTree

G = [(1, 1, 5), (6, 1, 2), (2, 2, 5), (1, 5, 6), (5, 2, 3), (6, 3, 4),
     (5, 3, 6), (3, 6, 7), (3, 7, 8), (5, 4, 6), (7, 4, 8), (2, 2, 6),
     (4, 3, 7)]

print primsAlgo(G, 0, 8)
