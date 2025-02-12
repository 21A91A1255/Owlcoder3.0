from collections import OrderedDict
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        l=[]
        d={}
        nums.sort()
        ans=0
        for i in range(len(nums)-1,-1,-1):
            s=0
            v=nums[i]
            while(nums[i]>0):
                n=nums[i]%10
                s+=n
                nums[i]=nums[i]//10
            if s in d:
                d[s].append(v)
                if(len(d[s])==2):
                    m=d[s][0]+d[s][1]
                    if(m>ans):
                        ans=m
            else:
                d[s]=[]
                d[s].append(v)
        if(ans!=0):
            return ans
        return -1
        