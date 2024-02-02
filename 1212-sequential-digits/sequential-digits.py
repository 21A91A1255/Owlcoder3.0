class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        p=len(str(low))
        q=len(str(high))
        l=['1','2','3','4','5','6','7','8','9']
        m=[]
        j=1
        while(j<=q):
            p=j
            for i in range(len(l)):
                d=l[i:i+p]
                n="".join(d)
                n=int(n)
                if(n>=low and n<=high):
                    m.append(n)
            j+=1
        s=set(m)
        v=sorted(s)
        return v