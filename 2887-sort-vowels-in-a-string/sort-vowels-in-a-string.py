class Solution:
    def sortVowels(self, s: str) -> str:
        o=set('AEIOUaeiou')
        s=list(s)
        b=0
        p=[]
        for i in s:
            if i in o:
                p.append(i)
        p.sort()
        for i,val in enumerate(s):
            if val in o:
                s[i]=p[b]
                b+=1
        m="".join(s)
        return m