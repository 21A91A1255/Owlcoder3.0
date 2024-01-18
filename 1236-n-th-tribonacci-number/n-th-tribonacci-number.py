class Solution:
    def tribonacci(self, n: int) -> int:
        a=0
        b=1
        c=1
        p=[]
        if(n==0):
            return 0
        elif(n==1 or n==2):
            return 1
        for i in range(n-2):
            t=a+b+c
            a=b
            b=c
            c=t
        return t

        
        