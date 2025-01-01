class Solution:
    def maxScore(self, s: str) -> int:
        m=0
        for i in range(len(s)-1):
            p=s[i+1:]
            q=s[:i+1]
            print(p)
            print(q)
            k=p.count('1')+q.count('0')
            if(k>m):
                m=k
        return m