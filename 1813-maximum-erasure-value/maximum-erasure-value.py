class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        s=set()
        l=0
        cs=0
        m=0
        for i in range(len(nums)):
            while nums[i] in s:
                s.remove(nums[l])
                cs-=nums[l]
                l+=1
            s.add(nums[i])
            cs+=nums[i]
            m=max(cs,m)
        return m
