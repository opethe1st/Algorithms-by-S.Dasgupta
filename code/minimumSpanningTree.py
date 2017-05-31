def Kruskal(G, n):
    """Given an undirected weighted Graph return it's minimum spanning tree
    Graph G is represented by a list of edges and weights, 
    n is the number of nodes"""
    parent = [0]*n
    rank = [0]*n

    def makeset(A):
        "make disjoint where every element is a singleton set"
        for a in A:
            parent[a] = a

    def find(u):
        "find the set u belongs to"
        while parent[u] != u:
            u = parent[u]
        return u

    def union(u, v):
        rootu = find(u)
        rootv = find(v)
        if rank[rootu] > rank[rootv]:
            parent[rootv] = rootu
        elif rank[u] < rank[v]:
            parent[rootu] = rootv
        else:
            rank[rootu] += 1
            parent[rootv] = rootu
    makeset(range(n))
    G.sort()
    MinSpanTree = set()
    for edge in G:
        w, u, v = edge
        if find(u) != find(v):
            MinSpanTree.add((w, u, v))
            union(u, v)
    return MinSpanTree
