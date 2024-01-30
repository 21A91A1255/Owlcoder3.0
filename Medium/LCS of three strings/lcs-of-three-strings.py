#User function Template for python3

class Solution:
    def lcs(self,s1,s2,s3,x,y,z):
        l=[[[0]*(z+1) for j in range(y+1)] for i in range(x+1)]
        for i in range(x+1):
            for j in range(y+1):
                for k in range(z+1):
                    if(i==0 or j==0 or k==0):
                        l[i][j][k]=0
                    elif(s1[i-1]==s2[j-1]==s3[k-1]):
                        l[i][j][k]=l[i-1][j-1][k-1]+1
                    else:
                        l[i][j][k]=max(l[i-1][j][k],l[i][j-1][k],l[i][j][k-1])
        return l[x][y][z]

    def LCSof3(self,A,B,C,n1,n2,n3):
        # code here
        d=self.lcs(A,B,C,n1,n2,n3)
        return d

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n1,n2,n3 = map(int,input().split())
        A,B,C = input().split()

        solObj = Solution()

        ans = solObj.LCSof3(A,B,C,n1,n2,n3)

        print(ans)
# } Driver Code Ends