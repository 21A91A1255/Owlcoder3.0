class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        
        ml = 0
        st = ""

        for i in range(n):
            # Odd length palindrome
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > ml:
                    ml = r - l + 1
                    st = s[l:r+1]
                l -= 1
                r += 1
            
            # Even length palindrome
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > ml:
                    ml = r - l + 1
                    st = s[l:r+1]
                l -= 1
                r += 1

        return st
      
                
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        ob = Solution()

        ans = ob.longestPalindrome(S)

        print(ans)
        print("~")
# } Driver Code Ends