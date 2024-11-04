//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C+
class Solution {
public:
    vector<vector<int>> findTriplets(vector<int> &arr) {
        map<int, vector<pair<int, int>>> mpp;
        int n = arr.size();
      
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                int s = arr[i] + arr[j];
                mpp[s].push_back(make_pair(i, j));  
            }
        }
        
        set<vector<int>> resSet;
        
        for (int k = 0; k < n; k++) {
            int su = -arr[k];
            if (mpp.find(su) != mpp.end()) {
                for (auto &p : mpp[su]) {
                    if (p.first != k && p.second != k) {
                        vector<int> curr = {k, p.first, p.second};
                        sort(curr.begin(), curr.end());
                        resSet.insert(curr);
                    }
                }
            }
        }
        
        return vector<vector<int>>(resSet.begin(), resSet.end());
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    cin.ignore();
    while (t--) {
        vector<int> arr;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }
        Solution ob;

        vector<vector<int>> res = ob.findTriplets(arr);
        sort(res.begin(), res.end());
        if (res.size() == 0) {
            cout << "[]\n";
        }
        for (int i = 0; i < res.size(); i++) {
            for (int j = 0; j < res[i].size(); j++) {
                cout << res[i][j] << " ";
            }
            cout << endl;
        }
        cout << "~" << endl;
    }
    return 0;
}
// } Driver Code Ends