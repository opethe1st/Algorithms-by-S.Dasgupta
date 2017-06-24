def solution(A):
    prefixSum = [0] * (len(A) + 1)
    for i in xrange(len(A)):
        prefixSum[i + 1] = prefixSum[i] + A[i]
    dp = [0] * len(A)
    for i in xrange(len(A)):
        maxval = -float('inf')
        for j in xrange(i+1):
            maxval = max(maxval, prefixSum[i+1] - prefixSum[j])
        dp[i] = maxval

    return max(dp)


def solution2(A):
    m = [0]*len(A)
    m[0] = A[0]
    for i in range(1, len(A)):
        m[i] = max(m[i-1]+A[i], A[i])
    return max(m)

print solution([5, 15, -30, 10, -5, 40, 10])
print solution2([5, 15, -30, 10, -5, 40, 10])
