class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int k=matrix.size();
        int arr[k][k];
        cout<<(k);
        for(int i=0;i<k;i++)
        {
            for(int j=0;j<k;j++)
            {
                arr[i][j]=matrix[(k-1)-j][i];
            }
        }
        for(int i=0;i<k;i++)
        {
            for(int j=0;j<k;j++)
            {
                matrix[i][j]=arr[i][j];
            }
        }

    }
};