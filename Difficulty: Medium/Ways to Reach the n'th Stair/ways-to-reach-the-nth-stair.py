
class Solution:
    def countWays(self, n):
        # code here
        l=[1,2]
        if(n==1 or n==2):
            return n
        for i in range(2,n):
            l.append(l[-1]+l[-2])
        return l[-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

sys.setrecursionlimit(10**6)

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob = Solution()
        print(ob.countWays(m))

        print("~")

# } Driver Code Ends