#User function Template for python3

class Solution:

    def countPS(self, s):
        # code here
        c=0
        n=len(s)
        for i in range(len(s)):
            l,r=i,i
            while(l>=0 and r<n and s[l]==s[r]):
                d=r-l+1
                if(d>=2):
                    c+=1
                l-=1
                r+=1
            l,r=i,i+1
            while(l>=0 and r<n and s[l]==s[r]):
                d=r-l+1
                if(d>=2):
                    c+=1
                l-=1
                r+=1
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.countPS(s))

        print("~")
# } Driver Code Ends