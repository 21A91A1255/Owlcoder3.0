//{ Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function Template for C++

class Solution
{
    public:
    vector<vector<int>>ans;
    void fun(vector<int>& A,vector<int>& curr,int i)
    {
        if(i==A.size())
        {
            ans.push_back(curr);
            return ;
        }
        fun(A,curr,i+1);
        curr.push_back(A[i]);
        fun(A,curr,i+1);
        curr.pop_back();
    }
    vector<vector<int> > subsets(vector<int>& A)
    {
        //code here
        vector<int>v;
        vector<int>curr;
        fun(A,curr,0);
        sort(ans.begin(),ans.end());
        return ans;
    }
};

//{ Driver Code Starts.

int main()
{
	int t;
	cin >> t;

	while (t--)
	{
		int n, x;
		cin >> n;

		vector<int> array;
		for (int i = 0; i < n; i++)
		{
			cin >> x;
			array.push_back(x);
		}
        
        
        Solution ob;
		vector<vector<int> > res = ob.subsets(array);

		// Print result
		for (int i = 0; i < res.size(); i++) {
			for (int j = 0; j < res[i].size(); j++)
				cout << res[i][j] << " ";
			cout << endl;
		}

		
	}

	return 0;
}
// } Driver Code Ends