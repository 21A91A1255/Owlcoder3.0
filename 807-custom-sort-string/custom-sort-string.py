from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ans=""
        p=""
        for i in order:
            if i in s:
                c=s.count(i)
                for j in range(c):
                    ans+=i
        for i in s:
            if i not in ans:
                p+=i
        k=(ans+p)
        return k