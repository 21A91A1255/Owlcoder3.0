class Solution:
    def countSubstr(self, s, k):
        c = 0
        n = len(s)
        for i in range(n):
            freq = {}
            distinct = 0
            for j in range(i, n):
                if s[j] not in freq:
                    freq[s[j]] = 1
                    distinct += 1
                else:
                    freq[s[j]] += 1
                if distinct == k:
                    c += 1
                elif distinct > k:
                    break
        return c
