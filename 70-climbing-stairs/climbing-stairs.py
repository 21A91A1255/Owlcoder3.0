
class Solution:
    def fab(self,n):
        a=0
        b=1
        if(n==0):
            return 0
        if(n==1):
            return n
        for i in range(1,n+1):
            t=a+b
            a=b
            b=t
        return b
    def climbStairs(self, n: int) -> int:
        return self.fab(n)


        