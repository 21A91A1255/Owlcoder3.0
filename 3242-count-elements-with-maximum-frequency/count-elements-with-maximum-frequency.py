from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        l=[]
        c=Counter(nums)
        for i in c.keys():
            l.append(c[i])
        l.sort()
        p=[]
        for i in range(len(l)-1,-1,-1):
            if(l[i]!=l[i-1]):
                p=l[i:len(l)]
                break
        if(len(p)==0):
            return len(nums)
        else:
            return sum(p)
        return 0