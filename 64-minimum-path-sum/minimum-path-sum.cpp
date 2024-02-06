#define ll long long
class Solution {
public:
    ll fun(int i,int j,vector<vector<int>>& grid,int m,int n, vector<vector<int>>& dp)
    {
        ll mini=INT_MAX;
        if(i>=m || j>=n) return INT_MAX;
        if(i==m-1 && j==n-1) return grid[i][j];
        if(dp[i][j]!=-1) return dp[i][j];
        ll a=grid[i][j]+fun(i,j+1,grid,m,n,dp);
        ll b=grid[i][j]+fun(i+1,j,grid,m,n,dp);
        return dp[i][j]=min(a, b);
    }
    int minPathSum(vector<vector<int>>& grid) {
        int m=grid.size(),n=grid[0].size();
        vector<vector<int>> dp(m+1, vector<int>(n+1, -1));
        return fun(0,0,grid,m,n, dp);
    }
};