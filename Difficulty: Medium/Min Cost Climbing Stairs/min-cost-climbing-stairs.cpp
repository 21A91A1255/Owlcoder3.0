//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

//Back-end complete function Template for C++

class Solution {
  public:
    int dp[100001];
    int minCost(int ind, vector<int>& cost) {
        if (ind >= cost.size()) return 0;  
        if (dp[ind] != -1) return dp[ind];
    
        int oneStep = cost[ind] + minCost(ind + 1, cost);
        int twoStep = cost[ind] + minCost(ind + 2, cost);
    
        return dp[ind] = min(oneStep, twoStep);
    }
    
    int minCostClimbingStairs(vector<int>& cost) {
        memset(dp, -1, sizeof(dp));
        return min(minCost(0, cost), minCost(1, cost)); 
    }

};


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    cin.ignore();

    while (t-- > 0) {
        string str;
        getline(cin, str);

        stringstream ss(str);
        vector<int> arr;
        int num;
        while (ss >> num) {
            arr.push_back(num);
        }
        Solution sln;
        int res = sln.minCostClimbingStairs(arr);
        cout << res << endl;
        cout << "~" << endl;
    }

    return 0;
}
// } Driver Code Ends