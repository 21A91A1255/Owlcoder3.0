class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        l=[]
        m=len(nums)
        k=(m*(m+1))//2
        s=sum(nums)
        t=set(nums)
        h=sum(t)
        p=sum(t)
        l.append(s-h)
        l.append(k-h)
        return l