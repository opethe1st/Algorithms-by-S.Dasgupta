visited = [False] * 11
prev = [-1] * 11
post = [-1] * 11

# this is wrong somehow..
def dfs(G, u):
    global clock
    #  visited = [False] * 11
    stack = [u]
    visited[u] = True
    # clock = 0
    prev[u] = clock
    clock += 1
    while stack:
        u = stack.pop(-1)
        print u,
        #visited[u] = True
        # this post value is wrong.
        post[u] = clock
        clock += 1
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)
                prev[v] = clock
                clock += 1

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

clock = 0
for node in xrange(1, 11):
    if not visited[node]:
        dfs(G, node)
        print
print prev
print post
