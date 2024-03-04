class Solution:
    import math
    def prime(self,n):
        l=[]
        while(n%2==0):
            n=n//2
            l.append(2)
        for i in range(3,int(math.sqrt(n)+1),2):
            while(n%i==0):
                l.append(i)
                n=n//i
        if(n>2):
            l.append(n)
        return l
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        ans=[]
        for i in range(len(nums)):
            d=self.prime(nums[i])
            ans+=d
        return len(set(ans))
    
        