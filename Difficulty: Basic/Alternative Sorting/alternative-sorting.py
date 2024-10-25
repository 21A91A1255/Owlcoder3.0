class Solution:
    def alternateSort(self,arr):
        # Your code goes here
        arr.sort()
        l=[]
        for i in range(len(arr)):
            if(len(arr)>1):
                l.append(arr[(len(arr)-i)-1])
                l.append(arr[i])
            if(i>=(len(arr)//2)-1):
                break
        if(len(arr)%2!=0):
            l.append(arr[(len(arr)//2)])
        return l


#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.alternateSort(arr)
        print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends