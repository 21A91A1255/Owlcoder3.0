class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        num_set = set(nums)
        m = 0
        for num in nums:
            c= 0
            current = num
            while current in num_set:
                c += 1
                current *= current 
            m= max(m, c)
        if(m==1):
            return -1
        else:
            return m
            


        