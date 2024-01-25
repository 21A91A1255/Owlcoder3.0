class Solution:
    def lcs(self,x,y,s1,s2):
        l=[[None]*(y+1) for i in range(x+1)]
        for i in range(x+1):
            for j in range(y+1):
                if(i==0 or j==0):
                    l[i][j]=0
                elif(s1[i-1]==s2[j-1]):
                    l[i][j]=l[i-1][j-1]+1
                else:
                    l[i][j]=max(l[i-1][j],l[i][j-1])
        return l[x][y]
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        x=len(s1)
        y=len(s2)
        d=self.lcs(x,y,s1,s2)
        return d