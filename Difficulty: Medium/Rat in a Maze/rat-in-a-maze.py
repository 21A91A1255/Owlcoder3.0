class Solution:
    def fun(self,i,j,n,maze,ans,res):
        if(i<0 or j<0 or i>=n or j>=n):
            return
        if(maze[i][j]==0 or maze[i][j]==2):
            return
        if(i==n-1 and j==n-1):
            res.append(ans)
            return 
        maze[i][j]=2
        self.fun(i-1,j,n,maze,ans+'U',res)
        self.fun(i+1,j,n,maze,ans+'D',res)
        self.fun(i,j-1,n,maze,ans+'L',res)
        self.fun(i,j+1,n,maze,ans+'R',res)
        maze[i][j]=1
    def ratInMaze(self, maze):
        ans=''
        res=[]
        n=(len(maze[0]))
        self.fun(0,0,n,maze,ans,res)
        return sorted(list(set(res)))