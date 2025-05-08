#User function Template for python3

class Solution:
    def findMissing(self, arr):
        n = len(arr) + 1 
        a = arr[0] 
        d1 = (arr[1] - arr[0])
        d2=(arr[2]-arr[1])
        d=min(d1,d2)
        esum = (n * (2 * a + (n - 1) * d)) // 2
        asum = sum(arr)
        return esum-asum


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import sys
import math


def main():
    input = sys.stdin.read
    data = input().strip().split('\n')

    t = int(data[0])
    solution = Solution()

    for i in range(1, t + 1):
        arr = list(map(int, data[i].split()))
        print(solution.findMissing(arr))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends