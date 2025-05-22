class Solution:
    def lcs(self,s,s1):
        n=len(s)
        m=len(s1)
        dp=[[0]*(m+1) for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if(s[i-1]==s1[j-1]):
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[m][n]
    def minDeletions(self,s):
        # code here 
        s1=str(s)
        s1=s1[::-1]
        d=self.lcs(s,s1)
        return len(s)-d
        