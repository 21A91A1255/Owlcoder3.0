class Solution:
    def minimumLength(self, s: str) -> int:
        i=0
        j=len(s)-1
        while(i<j):
            if(s[i]==s[j]):
                while(j>-1 and s[i]==s[j]):
                    j-=1
                while(i<j and s[j+1]==s[i]):
                    i+=1
            else : break
        l=(j-i)+1
        if(l<0):
            return 0
        return l
        