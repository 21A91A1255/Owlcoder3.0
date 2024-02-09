//{ Driver Code Starts
//Initial template for C++

#include<bits/stdc++.h> 
using namespace std; 

// } Driver Code Ends
//User function template for C++
class Solution {
public:
    int fun(vector<int>& arr, int sum, int i, vector<vector<int>>& dp) {
        if (i == arr.size()) {
            if(sum==0){
            return 1;
            }
            return 0;
        }
        if (dp[i][sum] != -1) {
            return dp[i][sum];
        }
        int a=0;
        if(sum>=arr[i]){
            a = fun(arr, sum - arr[i], i + 1, dp);
        }
        int b = fun(arr, sum, i + 1, dp);
        return dp[i][sum] = a + b;
    }

    bool isSubsetSum(vector<int> arr, int sum) {
        vector<vector<int>>dp(arr.size()+1,vector<int>(sum + 1, -1));
        return fun(arr, sum, 0, dp);
    }
};


//{ Driver Code Starts.
int main() 
{ 
    int t;
    cin>>t;
    while(t--)
    {
        int N, sum;
        cin >> N;
        vector<int> arr(N);
        for(int i = 0; i < N; i++){
            cin >> arr[i];
        }
        cin >> sum;
        
        Solution ob;
        cout << ob.isSubsetSum(arr, sum) << endl;
    }
    return 0; 
} 

// } Driver Code Ends