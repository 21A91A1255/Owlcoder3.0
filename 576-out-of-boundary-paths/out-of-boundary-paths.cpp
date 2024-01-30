class Solution {
public:
    long long int mod = 1000000007;
    long long int fun(int i,int j,int m,int n,int maxMove,vector<vector<vector<int>>>&dp)
    {
        if((i<0 || j<0 || i>=m || j>=n)&&(maxMove>=0))return 1;
        if(maxMove<=0)return 0;
        if(dp[i][j][maxMove]!=-1)return (dp[i][j][maxMove])%mod;
        long long int a=0,b=0,c=0,d=0;
        a=((a%mod)+(fun(i-1,j,m,n,maxMove-1,dp)%mod))%mod;
        b=((b%mod)+(fun(i+1,j,m,n,maxMove-1,dp)%mod))%mod;
        c=((c%mod)+(fun(i,j-1,m,n,maxMove-1,dp)%mod))%mod;
        d=((d%mod)+(fun(i,j+1,m,n,maxMove-1,dp)%mod))%mod;
        return dp[i][j][maxMove]=((((a%mod)+(b%mod))%mod+(c%mod))%mod+(d%mod)%mod);
    }
    int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        vector<vector<vector<int>>>dp(51,vector<vector<int>>(51,vector<int>(51,-1)));
        return fun(startRow,startColumn,m,n,maxMove,dp)%mod;
    }
};