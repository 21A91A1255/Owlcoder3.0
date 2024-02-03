class Solution {
public:
    int fun(int i,int j,vector<vector<int>>& obstacleGrid,int n, int m,vector<vector<int>>& dp)
    {
        if(i>=n || j>=m) return 0;
        if(obstacleGrid[i][j]==1) return 0;
        if(dp[i][j]!=-1) return dp[i][j];
        if(i==n-1 && j==m-1) return 1;
        int right=fun(i,j+1,obstacleGrid,n, m,dp);
        int down=fun(i+1,j,obstacleGrid,n, m,dp);
        return dp[i][j]=right+down;
    }
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int n=obstacleGrid.size(), m=obstacleGrid[0].size();
        vector<vector<int>>dp(n+1,vector<int>(m+1,-1));
        if(obstacleGrid[n-1][m-1]==1) return 0;
        int d=fun(0,0,obstacleGrid,n, m,dp);
        return d;
    }
};