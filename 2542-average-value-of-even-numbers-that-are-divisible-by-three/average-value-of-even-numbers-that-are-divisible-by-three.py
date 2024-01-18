class Solution:
    def averageValue(self, nums: List[int]) -> int:
        c=0
        m=0
        for i in range(len(nums)):
            if(nums[i]%3==0 and nums[i]%2==0):
                c+=1
                m+=nums[i]
        if(c==0):
            return 0
        else:
            k=m//c
            return k
        
        