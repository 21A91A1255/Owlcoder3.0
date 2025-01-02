#User function Template for python3

class Solution:
    def subArraySum(self,arr,k):  
        #code here
        d={}
        d[0]=1
        c=0
        ps=0
        for i in range(len(arr)):
            ps+=arr[i]
            r=ps-k
            if r in d:
                c+=d[r]
            if ps in d:
                d[ps]+=1
            else:
                d[ps]=1
        return c
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.subArraySum(arr, k)
        print(ans)
        tc -= 1
        print("~")

# } Driver Code Ends