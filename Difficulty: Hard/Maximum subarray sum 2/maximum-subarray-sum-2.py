from collections import deque

class Solution:
    def maxSubarrSum(self, arr, a, b):
        n = len(arr)
        prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + arr[i - 1]

        maxSum = -10**18
        dq = deque()

        for i in range(a, n + 1):
            while dq and dq[0] < i - b:
                dq.popleft()
            while dq and prefix[dq[-1]] >= prefix[i - a]:
                dq.pop()
            dq.append(i - a)
            maxSum = max(maxSum, prefix[i] - prefix[dq[0]])

        return maxSum
