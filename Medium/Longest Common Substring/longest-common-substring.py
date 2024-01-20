#User function Template for python3

class Solution:
    def longestCommonSubstr(self, s1,s2,x,y):
        # code here
        k=[]
        l=[[None]*(y+1) for i in range(x+1)]
        for i in range(x+1):
            for j in range(y+1):
                if(i==0 or j==0):
                    l[i][j]=0
                elif(s1[i-1]==s2[j-1]):
                    l[i][j]=l[i-1][j-1]+1
                    k.append(l[i][j])
                else:
                    l[i][j]=0
        if(len(k)!=0):
            return max(k)
        return 0
    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n,m = input().strip().split(" ")
        n,m = int(n), int(m)
        S1 = input().strip()
        S2 = input().strip()
        
        
        ob=Solution()
        print(ob.longestCommonSubstr(S1, S2, n, m))
# } Driver Code Ends