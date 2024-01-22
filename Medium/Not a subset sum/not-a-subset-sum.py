#User function Template for python3

class Solution:
    def findSmallest(self, arr, n):
        # code here
        r=1
        for i in range(0,n):
            if(arr[i]<=r):
                r=r+arr[i]
            else:
                break
        return r
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findSmallest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends