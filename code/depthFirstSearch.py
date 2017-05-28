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

"""
clock = 0
for node in range(9):
    if not visited[node]:
        dfs(G, node)
print

print pre
print post
"""
# 3.2 New Graph

G2 = [[] for i in range(8)]
G2[0].append(1)
G2[0].append(5)
G2[1].append(2)
G2[1].append(4)
G2[2].append(3)
G2[3].append(1)
G2[3].append(7)
G2[4].append(3)
G2[4].append(6)
G2[5].append(6)
G2[5].append(4)
G2[6].append(5)
G2[7].append(6)

G3 = [[] for i in range(8)]
G3[0].append(2)
G3[1].append(2)
G3[2].append(3)
G3[2].append(4)
G3[3].append(5)
G3[4].append(5)
G3[5].append(6)
G3[5].append(7)

clock = 0
for node in range(8):
    if not visited[node]:
        dfs(G3, node)
        print
print

print pre
print post