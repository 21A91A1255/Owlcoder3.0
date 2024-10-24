#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def modifyAndRearrangeArr (self, arr) : 
        l=[]
        for i in range(len(arr)-1):
            if(arr[i]==arr[i+1] and (arr[i]!=0 and arr[i+1]!=0)):
                arr[i]=arr[i]*2
                arr[i+1]=0
        m=[]
        p=[]
        for i in range(len(arr)):
            if(arr[i]!=0):
                p.append(arr[i])
            else:
                m.append(0)
        l=p+m
        return l


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.modifyAndRearrangeArr(arr)
        print(*ans)
        print("~")
        t -= 1


# } Driver Code Ends