def merge(x, y):
    # print x,y
    if x == []:
        return y
    if y == []:
        return x
    if x[0] < y[0]:
        return [x[0]] + merge(x[1:], y)
    else:
        return [y[0]] + merge(x, y[1:])


def mergesort(A):
    x = A[:len(A) / 2]
    y = A[len(A) / 2:]
    if len(A) == 1:
        return A
    return merge(mergesort(x), mergesort(y))


print mergesort([112, 12, 1, 243, 233, 1, 290, 68])


def itermergesort(A):
    q = [[a] for a in A]
    while len(q) != 1:
        val1 = q.pop(0)
        val2 = q.pop(0)
        q.append(merge(val1, val2))
    return q[0]


print itermergesort([112, 12, 1, 243, 233, 1, 290, 68])
