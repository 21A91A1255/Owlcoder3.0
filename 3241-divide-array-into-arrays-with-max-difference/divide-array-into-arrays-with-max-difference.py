class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        ans=[]
        if((nums[n-1]-nums[n-2])>k):
            return []
        else:
            i=0
            m=3
            d=0
            while(i<n):
                c=0
                p=nums[i:m]
                d+=1
                if(p[1]-p[0]<=k and p[2]-p[0]<=k and p[2]-p[1]<=k):
                    c+=1
                if(c==1):
                    ans.append(p)
                i+=3
                m+=3
            if(d==len(ans)):
                return ans
            else:
                return []