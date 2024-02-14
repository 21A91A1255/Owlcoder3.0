class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p=[]
        m=[]
        for i in range(len(nums)):
            if(nums[i]>0):
                p.append(nums[i])
            else:
                m.append(nums[i])
        ans=[]
        for i in range(len(p)):
            ans.append(p[i])
            ans.append(m[i])
        return ans
        


        
        