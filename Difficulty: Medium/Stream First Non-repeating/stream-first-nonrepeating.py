from collections import deque
class Solution:
    def firstNonRepeating(self, s):
        ans = ""
        freq = {}
        q=deque()
        for i in s:
            freq[i]=freq.get(i,0)+1
            q.append(i)
            while q and freq[q[0]]>1:
                q.popleft()
            if q:
                ans+=q[0]
            else:
                ans+='#'
        return ans
