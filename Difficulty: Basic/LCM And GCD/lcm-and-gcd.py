#User function Template for python3
class Solution:
    def hcf(self,a,b):
        while(a>0 and b>0):
            if(a>b):
                a=a%b
            else:
                b=b%a
        if(a==0):
            return b
        return a
    def lcmAndGcd(self, A , B):
        # code here 
        r=[]
        h=self.hcf(A,B)
        l=(A*B)//h
        r.append(l)
        r.append(h)
        return r


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B=map(int,input().split())
        
        ob = Solution()
        ptr = ob.lcmAndGcd(A,B)
        
        print(ptr[0],ptr[1])
# } Driver Code Ends