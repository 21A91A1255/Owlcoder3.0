class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        c=0
        d=0
        for i in range(len(nums)):
            if(nums[i]<0):
                c+=1
            if(nums[i]>0):
                d+=1
        return max(c,d)
        