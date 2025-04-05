class Solution:
    def rec(self, i, xor, n, nums):
        if i == n:

            return xor
        if i > n:
            return 0

        pick = self.rec(i + 1, xor ^ nums[i], n, nums)
        dont = self.rec(i + 1, xor, n, nums)
        return pick + dont

    def subsetXORSum(self, nums):
        n = len(nums)
        return self.rec(0, 0, n, nums)