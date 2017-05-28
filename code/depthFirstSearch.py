visited = [False] * 9
pre = [-1] * 9
post = [-1] * 9
G = [[] for i in range(9)]
G[0] = [1, 4]
G[1] = [1, 2, 4]
G[2] = [1, 5]
G[3] = [6, 7]
G[4] = [1, 5]
G[5] = [4, 8]
G[6] = [3, 7]
G[7] = [3, 6]
G[8] = [5]

num2letter = dict(zip(range(9), 'ABCDEFGHI'))


def dfs(G, u):
    global clock
    global visited
    pre[u] = clock
    clock += 1
    visited[u] = True
    print num2letter[u],
    for v in G[u]:
        if not visited[v]:
            dfs(G, v)
    post[u] = clock
    clock += 1


clock = 0
# for node in range(9):
#    if not visited[node]:
#        dfs(G, node)
#        print
dfs(G, 0)
print

print pre
print post
