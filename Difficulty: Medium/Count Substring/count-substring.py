class Solution:
    def countSubstring(self, s):
        ans = 0
        i=0
        j=0
        freq={}
        c=0
        for i in range(len(s)):
            freq[s[i]]=freq.get(s[i],0)+1
            if(freq[s[i]]==1):
                c+=1
            while c>=3:
                ans+=len(s)-i
                freq[s[j]]-=1
                if(freq[s[j]]==0):
                    c-=1
                j+=1
        return ans
