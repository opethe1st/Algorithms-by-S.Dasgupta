# reference
print 13466 * 3433344


def multp(x, y):
    """Al Khwarizmi's algorithm"""
    ans = 0
    while x > 0:
        if x & 1 == 1:
            ans += y
        x /= 2
        y *= 2
    return ans


# test
print multp(13466, 3433344)


def multp2(x, y):
    """ multiplication ala francais"""
    if y == 0:
        return 0
    else:
        if y & 1:
            return x + 2 * multp2(x, y / 2)
        else:
            return 2 * multp2(x, y / 2)


# test
print multp2(13466, 3433344)


def divide(x, y):
    if x == 0:
        return (0, 0)
    else:
        q, r = divide(x / 2, y)
        q = 2 * q
        r = 2 * r
        if x & 1:
            r += 1
        if r >= y:
            r = r - y
            q = q + 1
        return (q, r)


print divide(46233410304, 13466)
