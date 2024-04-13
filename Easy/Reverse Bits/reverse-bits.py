#User function Template for python3

class Solution:
    def reversedBits(self, x):
        # code here 
        b=bin(x)[2:]
        r=b[::-1]
        r= r.ljust(32, '0')
        p=int(r,2)
        return p


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        X=int(input())
        
        ob = Solution()
        print(ob.reversedBits(X))
# } Driver Code Ends