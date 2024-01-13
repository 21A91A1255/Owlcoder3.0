class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c=0
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in t:
            if i in d:
                d[i]-=1
            else:
                d[i]=-1
        for i in d.values():
            if(i<0):
                c+=(i*(-1))
        return c

