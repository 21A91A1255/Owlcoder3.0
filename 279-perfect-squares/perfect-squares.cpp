class Solution {
public:
    int dp[100001];
    int fun(int p,vector<int>& arr,int k)
    {
        if(k==0) return 0;
        if(dp[k]!=-1) return dp[k];
        int mini=INT_MAX;
        for(int i=0;i<p;i++)
        {
            if(arr[i]<=k)
            {
                mini=min(mini,1+fun(p,arr,k-arr[i]));
            }
        }
        return dp[k]=mini;
    }
    int numSquares(int n) {
        vector<int>arr;
        int k=n;
        for(int i=1;i<=k;i++)
        {
            int d=sqrt(i);
            if(i==d*d){
                arr.push_back(i);
            }
        }
        memset(dp,-1,sizeof(dp));
        int p=arr.size();
        return fun(p,arr,k);
    }

};