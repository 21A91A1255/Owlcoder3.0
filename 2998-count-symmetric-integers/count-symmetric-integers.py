class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        c=0
        for i in range(low,high+1,1):
            i=str(i)
            s=len(str(i))
            if(s%2==0):
                s1=i[:s//2]
                s2=i[s//2:]
                d=0
                for i in range(len(s1)):
                    d+=int(s1[i])
                p=0
                for i in range(len(s2)):
                    p+=int(s2[i])
                if(d==p):
                    c+=1
        return c      