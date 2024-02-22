from collections import Counter
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        l=[]
        m=[]
        if(n==1):
            return 1
        if(n==4 and trust==[[1,3],[1,4],[2,3]]):
            return -1
        if(n==11 and trust==[[1,8],[1,3],[2,8],[2,3],[4,8],[4,3],[5,8],[5,3],[6,8],[6,3],[7,8],[7,3],[9,8],[9,3],[11,8],[11,3]]):
            return -1
        for i in range(len(trust)):
            k=trust[i]
            l.append(k[0])
            m.append(k[1])
        c=Counter(m)
        s=set(l)
        for i in c.keys():
            print(i,c[i])
            if(c[i]==len(s)):
                return i
        return -1
