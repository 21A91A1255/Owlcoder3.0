class Solution:
    def minimumLength(self, s: str) -> int:
        i=0
        j=len(s)-1
        while(i<j and s[i]==s[j]):
            while(j>-1 and s[i]==s[j]):
                j-=1
            while(i<j and s[j+1]==s[i]):
                i+=1
        return j-i+1