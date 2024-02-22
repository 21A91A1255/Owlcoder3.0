from collections import Counter
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        l=[0]*(n+1)
        m=[0]*(n+1)
        for i in trust:
            p=i[0]
            q=i[1]
            l[p]+=1
            m[q]+=1
        for i in range(1,(n+1)):
            if(l[i]==0 and m[i]==n-1):
                return i
        return -1
        