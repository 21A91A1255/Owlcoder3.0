class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        m1=m2=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                p=nums[i:j]
                v=set(p)
                s=sorted(v)
                d=list(v)
                r=s[::-1]
                if(s==p):
                    m1=max(m1,len(s))
                if(r==p):
                    m2=max(m2,len(r))
        print(m1,m2)
        return max(m1,m2)
            