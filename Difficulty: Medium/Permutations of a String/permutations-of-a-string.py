#User function Template for python3
from itertools import permutations
class Solution:
    def findPermutation(self, s):
        # Code here
        l=[]
        p=permutations(s)
        for i in list(p):
            #print(i)
            d=''.join(i)
            l.append(d)
        k=set(l)
        l=list(k)
        return l
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        S = input()
        ob = Solution()
        ans = ob.findPermutation(S)
        ans.sort()
        for i in ans:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends