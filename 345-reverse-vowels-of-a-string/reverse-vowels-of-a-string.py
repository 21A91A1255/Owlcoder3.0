class Solution:
    def reverseVowels(self, s: str) -> str:
        o=set('AEIOUaeiou')
        s=list(s)
        t=[]
        p=0
        for i in s:
            if i in o:
                t.append(i)
        t=t[::-1]
        for i,val in enumerate(s):
            if val in o:
                s[i]=t[p]
                p+=1
        m="".join(s)
        return m
