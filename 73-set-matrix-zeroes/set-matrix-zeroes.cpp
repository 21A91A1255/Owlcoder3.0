class Solution {
public:
    void setZeroes(vector<vector<int>>& arr) {
        int m=arr.size(),n=arr[0].size();
        vector<int> row(m, 0);
        vector<int> col(n, 0);
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(arr[i][j]==0)
                {
                    row[i]=1;
                    col[j]=1;
                }
            }
        }
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(row[i]==1 or col[j]==1)
                {
                    arr[i][j]=0;
                }
            }
        }
        return ;
    }
};