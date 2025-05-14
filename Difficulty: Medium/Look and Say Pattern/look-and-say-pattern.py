class Solution:
    def countAndSay(self, n):
        curr = "1"
        if n == 1:
            return curr
        for _ in range(1, n):
            res = ""
            count = 1
            for j in range(1, len(curr)):
                if curr[j] == curr[j - 1]:
                    count += 1
                else:
                    res += str(count) + curr[j - 1]
                    count = 1
            res += str(count) + curr[-1]
            curr = res
        return curr

        
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n = int(input())

        solObj = Solution()

        print(solObj.countAndSay(n))

        print("~")
# } Driver Code Ends