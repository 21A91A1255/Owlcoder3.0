#User function Template for python3
import sys
class Solution:
    def printClosest (self,arr, brr, n, m, x) :
        i=0
        j=m-1
        a=0
        b=0
        l=[]
        s=0
        diff=sys.maxsize
        while(i<n and j>=0):
            s=arr[i]+brr[j]
            if(abs(s-x)<diff):
                diff=abs(s-x)
                a=arr[i]
                b=brr[j]
            if(s>x):
                j-=1
            else:
                i+=1
        l.append(a)
        l.append(b)
        return l
#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().strip().split()))
    brr = list(map(int, input().strip().split()))
    x = int(input())
    ob = Solution()
    ans = ob.printClosest(arr, brr, n, m, x)
    print(abs(ans[0]+ans[1] - x))
# } Driver Code Ends