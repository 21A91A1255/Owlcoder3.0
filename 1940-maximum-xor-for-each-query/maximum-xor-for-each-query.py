class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        p=''
        for i in range(maximumBit):
            p+='0'
        d=0
        l=[]
        x=[]
        for i in range(len(nums)):
            d=d^nums[i]
            x.append(d)
        #print(x)
        x=x[::-1]
        for i in range(len(x)):
            d=x[i]
            b=bin(d)[2:]
            v=''
            for k in range(len(p)-len(b)):
                v+='0'
            v=v+b
            n=''
            for i in range(len(v)):
                if(v[i]=='1'):
                    n+='0'
                else:
                    n+='1'
            l.append(int(n,2))
        return l
        