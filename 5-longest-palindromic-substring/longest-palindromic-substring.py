class Solution:
    def longestPalindrome(self, s: str) -> str:
        l=[]
        m=0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                p=s[i:j]
                if(p==p[::-1]):
                    l.append(p)
                    if(len(p)>m):
                        m=len(p)
        for i in range(len(l)):
            if(len(l[i])==m):
                return l[i]

        