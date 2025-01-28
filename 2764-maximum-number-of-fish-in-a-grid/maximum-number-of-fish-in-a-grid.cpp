class Solution {
public:
    int dfs(int i, int j, vector<vector<int>>& grid, int n, int m) {
        if (i < 0 || i >= n || j < 0 || j >= m || grid[i][j] == 0) 
            return 0;

        int fish = grid[i][j];
        grid[i][j] = 0; 
        fish += dfs(i + 1, j, grid, n, m);
        fish += dfs(i - 1, j, grid, n, m);
        fish += dfs(i, j + 1, grid, n, m);
        fish += dfs(i, j - 1, grid, n, m);
        return fish;
    }

    int findMaxFish(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        int maxFish = 0;
        vector<int>l;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (grid[i][j] > 0) {
                    //cout<<dfs(i, j, grid, n, m)<<" ";
                    l.push_back(dfs(i, j, grid, n, m));
                    //maxFish = max(maxFish, dfs(i, j, grid, n, m));
                }
            }
        }
        if(l.empty()) return 0;
        return *max_element(l.begin(),l.end());
    }
};
