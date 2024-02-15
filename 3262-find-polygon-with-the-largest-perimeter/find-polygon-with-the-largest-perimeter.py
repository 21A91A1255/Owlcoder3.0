class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        m=0
        x=sum(nums[:2])
        d=x
        for i in range(2,len(nums)):
            print(nums[i])
            d=d+nums[i]
            v=d-nums[i]
            if(nums[i]<v):
                if(d>m):
                    m=d;
        if(m==0):
            return -1
        return m
        



        