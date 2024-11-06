class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        p=sorted(nums)
        s=[]
        if(nums==p):
            return True
        else:
            for i in range(len(nums)):
                for j in range(len(nums)-1):
                    d=bin(nums[j])[2:]
                    c=d.count('1')
                    d1=bin(nums[j+1])
                    c1=d1.count('1')
                    if(nums[j]>nums[j+1] and c==c1):
                        (nums[j],nums[j+1])=(nums[j+1],nums[j])
                if(nums==p):
                    return True
            return False


            
        