class Solution {
public:
    int fun(int ind,vector<int>& cost,int n,vector<int>& dp)
    {
        if(ind>=n) return 0;
        if(dp[ind]!=-1) return dp[ind];
        int one=cost[ind]+fun(ind+1,cost,n,dp);
        int two=cost[ind]+fun(ind+2,cost,n,dp);

        return dp[ind]=min(one,two);
    }
    int minCostClimbingStairs(vector<int>& cost) {
        int n=cost.size();
        vector<int>dp(n+1,-1);
        int p=fun(0,cost,n,dp);
        int q=fun(1,cost,n,dp);
        return min(p,q);
    }
};