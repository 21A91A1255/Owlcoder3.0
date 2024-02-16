from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c=Counter(arr)
        y=OrderedDict(c.most_common())
        m=[]
        p=[]
        for i in y.keys():
            m.append(i)
            p.append(y[i]) 
        l=len(m)
        for i in range(len(p)-1,-1,-1):
            if(p[i]<=k):
                k=k-p[i]
                l=l-1
            else:
                return l
        return 0