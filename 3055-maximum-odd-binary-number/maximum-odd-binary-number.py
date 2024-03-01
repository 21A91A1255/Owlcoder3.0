class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        c=s.count('1')
        d=s.count('0')
        ans=""
        for i in range(c-1):
            ans+='1'
        for j in range(d):
            ans+='0'
        ans+='1'
        return ans