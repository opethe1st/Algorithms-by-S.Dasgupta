
def multiply(a, b):
    """numbers a and b represented as binary strings"""
    if a == "1":
        return b
    elif a == "0":
        return "0"
    else:
        m = a[:len(a) / 2]  # a>>length/2
        n = a[len(a) / 2:]
        o = b[:len(b) / 2]  # b>>length/2
        p = b[len(b) / 2:]
        p1 = multiply(m, n)
        p2 = multiply(o, p)
        p3 = multiply(int(m) + int(n), int(o) + int(p))
        return int(p1) << len(a) + (int(p3) - int(p1) - int(p2)) << (len(a)/2)\
            + int(p2)
