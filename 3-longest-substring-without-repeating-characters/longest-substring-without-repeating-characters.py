class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d=set()
        l=0
        m=0
        j=0
        for i in range(len(s)):
            while s[i] in d:
                d.remove(s[j])
                l-=1
                j+=1
            d.add(s[i])
            l+=1
            m=max(m,l)
        return m



        