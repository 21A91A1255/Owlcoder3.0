class Solution {
public:
    int dp[10000001];
    int fun(vector<int>& arr,int n,int k)
    {
        if(k==0) return 0;
        if(dp[k]!=-1) return dp[k];
        int mini=INT_MAX;
        for(int i=0;i<n;i++)
        {
            if(arr[i]<=k){
                int p=fun(arr,n,k-arr[i]);
                if(p!=INT_MAX){
                    mini=min(mini,1+p);
                }
            }
        }
        return dp[k]=mini;


    }
    int coinChange(vector<int>& arr, int k) {
        int n=arr.size();
        cout<<n;
        memset(dp,-1,sizeof(dp));
        int a=fun(arr,n,k);
        if(a==INT_MAX) return -1;
        else return a;
    }
};