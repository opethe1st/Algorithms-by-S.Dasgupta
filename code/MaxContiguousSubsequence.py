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


print solution([5, 15, -30, 10, -5, 40, 10])
