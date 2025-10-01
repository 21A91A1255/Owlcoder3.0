class Solution {
  public:
    int solve(int i, vector<int>& arr, int target, int n, vector<vector<int>>& dp) {
        if (i == n){
            if(target==0){
                return 1;
            }
            return 0;
        };           
        
        if (dp[i][target] != -1) return dp[i][target];
        
        int nonpick = solve(i + 1, arr, target, n, dp);
        int pick = 0;
        if (arr[i] <= target) {
            pick = solve(i + 1, arr, target - arr[i], n, dp);
        }
        
        return dp[i][target] = pick + nonpick;
    }
    
    int perfectSum(vector<int>& arr, int target) {
        int n = arr.size();
        vector<vector<int>> dp(n, vector<int>(target + 1, -1));
        return solve(0, arr, target, n, dp);
    }
};
