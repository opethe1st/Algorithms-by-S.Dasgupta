num2letter = dict(zip(range(14), ' ABCDEFGHIJKLM'))
clock = 0


def dfs(G, n):
    global clock
    visited = [False] * (n + 1)
    pre = [-1] * (n + 1)
    post = [-1] * (n + 1)
    order = []
    clock = 0

    def dfsVisit(G, u):
        global clock
        pre[u] = clock
        clock += 1
        visited[u] = True
        # print num2letter[u],
        for v in G[u]:
            if not visited[v]:
                dfsVisit(G, v)
        post[u] = clock
        order.append(u)
        clock += 1

    for node in xrange(1, n + 1):
        if not visited[node]:
            dfsVisit(G, node)
    return order


def getSCC(G, n):
    component = [0] * (n + 1)

    def dfsVisit(G, u, c):
        visited[u] = True
        component[u] = c
        s.add(num2letter[u])
        for v in G[u]:
            if not visited[v]:
                dfsVisit(G, v, c)
    order = dfs(G, n)
    visited = [False] * (n + 1)
    c = 0
    for node in order:
        if not visited[node]:
            s = set()
            c += 1
            dfsVisit(G, node, c)
            print s
    return component


G = [[] for i in range(11)]
G[1] = [3, 8]
G[2] = [1, 7]
G[3] = [4]
G[4] = [6]
G[5] = [1, 9]
G[6] = [10]
G[7] = [9]
G[8] = [6, 7]
G[9] = [8]
G[10] = [3]

print getSCC(G, 10)
