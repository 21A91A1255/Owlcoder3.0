#User function Template for python3

class Solution:
    def sumMatrix(self, n, q):
        # code here 
        if(q>n*n and q!=2):
            return 0
        t=n*2
        d=(t+2)//2
        a=(d-q)
        a=abs(a)
        if((n-a)<0):
            return 0
        return n-a


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())

        ob = Solution()
        print(ob.sumMatrix(n, q))

# } Driver Code Ends