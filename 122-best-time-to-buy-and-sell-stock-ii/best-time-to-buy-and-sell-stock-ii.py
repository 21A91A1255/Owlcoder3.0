class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        maxp=0
        ans=0
        while(r<len(prices) and l<len(prices)):
            if(prices[l]<prices[r]):
                pro=prices[r]-prices[l]
                print(pro)
                ans+=pro
            l+=1
            r+=1
        return ans

