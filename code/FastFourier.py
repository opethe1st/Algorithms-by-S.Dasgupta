from math import cos, sin, pi


def FFT(A, w):
    """A is a polynomial of degree 2^k=n. (pad with zeros if necessary), w is
    the kth root of unity. This function takes the coefficent expansion of the
    polynomical and returns the value representation of the polynomial
    """
    if len(A) == 1:
        return A
    Aodd = [A[i] for i in xrange(1, len(A), 2)]
    Aeven = [A[i] for i in xrange(0, len(A), 2)]
    Aoddvalues = FFT(Aodd, w**2)
    Aevenvalues = FFT(Aeven, w**2)
    Ans = []
    for i in xrange(len(A)/2):
        Ans.append(Aevenvalues[i] + w**i * Aoddvalues[i])
    for i in xrange(len(A)/2):
        Ans.append(Aevenvalues[i] - w**i * Aoddvalues[i])
    return Ans


def form(val):
    if abs(val) < 1e-9:
        return 0
    else:
        return int(val+0.5)

n = 8
w = cos(2*pi / n) + 1j * sin(2*pi / n)
ValueRep1 = FFT([0, 1, 2, 0, 0, 0, 0, 0], w)
ValueRep2 = FFT([2, 3, 8, 0, 0, 0, 0, 0], w)
ValueRep3 = [ValueRep1[i]*ValueRep2[i] for i in xrange(n)]
CoefficientRep3 = FFT(ValueRep3, 1/w)
ans = 0
power = 1
for val in CoefficientRep3:
    ans = form(val.real/n)*power+ans
    power *= 10
print ans
print [form(val.real/n) for val in CoefficientRep3]
print 210*832