class Solution:
    def check(self, nums: List[int]) -> bool:
        k=sorted(nums)
        for i in range(len(nums)):
            p=nums[:i]
            q=nums[i:]
            s=q+p
            #print(s)
            if(k==s):
                return True
        return False
