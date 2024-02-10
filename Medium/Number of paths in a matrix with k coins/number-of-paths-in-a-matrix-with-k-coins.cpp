//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
public:
    int c=0;
    long long dp[101][101][101];
    int fun(int i,int j,int n,int k,vector<vector<int>> &arr)
    {
        if(i>=n || j>=n) return 0;
        if(i==n-1 and j==n-1) {
            if(k==arr[i][j])
            {
                return 1;
            }
            return 0;
        }
        if(dp[i][j][k]!=-1) return dp[i][j][k];
        if(k<0) return 0;
        int a=0,b=0;
        a=fun(i+1,j,n,k-arr[i][j],arr);
        b=fun(i,j+1,n,k-arr[i][j],arr);
        return dp[i][j][k]=a+b;
    }
    long long numberOfPath(int n, int k, vector<vector<int>> arr){
        memset(dp,-1,sizeof(dp));
        return fun(0,0,n,k,arr);
    }
};

//{ Driver Code Starts.

int main()
{
    Solution obj;
    int i,j,k,l,m,n,t;
    cin>>t;
    while(t--)
    {
        cin>>k>>n;
        vector<vector<int>> v(n+1, vector<int>(n+1, 0));
        for(i=0;i<n;i++)
            for(j=0;j<n;j++)
                cin>>v[i][j];
        cout << obj.numberOfPath(n, k, v) << endl;
    }
}
// } Driver Code Ends