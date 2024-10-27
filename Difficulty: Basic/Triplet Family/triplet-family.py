class Solution:
    def findTriplet(self, arr):
        # Sort the array to enable searching only in the remaining part of the array for each element
        arr.sort()
        n = len(arr)
        
        # Iterate through each unique pair (i, j)
        for i in range(n - 1):
            for j in range(i + 1, n):
                s = arr[i] + arr[j]
                # Use a hash set to check if the sum exists in the remaining elements
                if s in arr[j + 1:]:
                    return True
        return False
                
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
# Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.findTriplet(arr)
        if (res):
            print("true")
        else:
            print("false")
        # print(res)
        print("~")
        t -= 1

# } Driver Code Ends