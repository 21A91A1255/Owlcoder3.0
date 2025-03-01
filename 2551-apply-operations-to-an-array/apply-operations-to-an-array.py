class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if(nums[i]==nums[i+1]):
                nums[i]=nums[i]*2
                nums[i+1]=0
        n=[]
        m=[]
        for i in range(len(nums)):
            if(nums[i]!=0):
                n.append(nums[i])
            else:
                m.append(nums[i])
        return n+m

