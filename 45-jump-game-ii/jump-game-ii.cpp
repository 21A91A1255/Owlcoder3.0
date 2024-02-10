class Solution {
public:
    int dp[10001];
    int fun(int ind,vector<int>& nums,int n)
    {
        if(ind>=n) return 0;
        if(dp[ind]!=-1) return dp[ind];
        if(ind==n-1) return 0;
        int k=nums[ind];
        if(ind+k>=n-1)return 0;
        int mini=1e4;
        for(int i=ind+1;i<=ind+k && i<n;i++)
        {
            mini=min(mini,1+fun(i,nums,n));
        }
        return dp[ind]=mini;
    }
    int jump(vector<int>& nums) {
        int n=nums.size();
        if(n==1)return 0;
        memset(dp,-1,sizeof(dp));
        return 1+fun(0,nums,n);
    }
};