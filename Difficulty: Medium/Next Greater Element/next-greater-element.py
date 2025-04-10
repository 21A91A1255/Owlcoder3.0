# User function Template for python3

class Solution:
    def nextLargerElement(self, arr):
        n = len(arr)
        ans = [-1] * n
        stack = []
        
        for i in range(n - 1, -1, -1): 
            while stack and stack[-1] <= arr[i]:
                stack.pop()
            if stack:
                ans[i] = stack[-1]
            stack.append(arr[i])
        
        return ans


#{ 
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().nextLargerElement(arr)  # find the next greater elements

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print next greater elements
    else:
        print("[]")  # Print empty list if no next greater element is found
    print("~")
# } Driver Code Ends