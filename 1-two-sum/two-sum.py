class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length=len(nums)
        l=[]
        for i in range(length):
            for j in range(i+1,length):
                if(nums[i]+nums[j]==target and i!=j):
                    l.append(i)
                    l.append(j)
        return l