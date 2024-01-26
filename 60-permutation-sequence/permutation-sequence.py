from itertools import permutations
class Solution:
    def fac(self,n):
        if(n==0 or n==1):
            return 1
        else:
            return n*self.fac(n-1)
    def getPermutation(self, n: int, k: int) -> str:
        t=self.fac(n)//n
        s=self.fac(n)
        x=s-k
        c=n
        while(s>=k):
            s=s-t
            c-=1
        s=s
        c=c+1
        l=[]
        l.append(c)
        for i in range(1,(n+1)):
            if i not in l:
                l.append(i)
        r=0
        p=permutations(l)
        y=s
        for i in list(p):
            r+=1
            y+=1
            if(y==k):
                m=i
            if(r==t):
                break
        m=list(m)
        for i in range(len(m)):
            m[i]=str(m[i])
        res="".join(m)
        return res




        