#User function Template for python3

class Solution:
    def maxSum(self,arr):
        # code here
        arr.sort()
        n=len(arr)
        l=[]
        for i in range(n//2):
            l.append(arr[i])
            l.append(arr[(n-i)-1])
        if(n%2!=0):
            l.append(arr[n//2])
        s=0
        for i in range(len(l)-1):
            s+=abs(l[i]-l[i+1])
        s+=abs(l[-1]-l[0])
        return s


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.maxSum(arr)  # Call maxSum method and store result in ans
        print(ans)  # Print the result
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends