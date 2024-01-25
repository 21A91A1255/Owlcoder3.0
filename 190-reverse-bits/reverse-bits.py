class Solution:
    def reverseBits(self, n: int) -> int:
        p=bin(n)[2:]
        p=p[::-1]
        if(len(p)<32):
            for i in range(len(p),32,1):
                p+='0'
        return int(p,2)
        

        