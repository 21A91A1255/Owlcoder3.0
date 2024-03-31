#User function Template for python3

class Solution:
    def series(self, n):
        # Code here
        m=1000000007
        l=[]
        q=0
        r=1
        l.append(q)
        l.append(r)
        for i in range(n-1):
            t=q%m+r%m
            q=r%m
            r=t%m
            l.append(t%m)
        return l


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        result = ob.series(N)
        print(*result)
# } Driver Code Ends