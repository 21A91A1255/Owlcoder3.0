//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
  public:
    int countTriplets(vector<int>& arr, int target) {
        int c = 0;
        int n = arr.size();

        for (int i = 0; i < n - 2; i++) {
            int j = i + 1, k = n - 1;

            while (j < k) {
                int triplet_sum = arr[i] + arr[j] + arr[k];

                if (triplet_sum == target) {
                    c++;
                    int t = j + 1;
                    while (t < k && arr[t] == arr[t - 1]) {
                        c++;
                        t++;
                    }
                    k--;
                } else if (triplet_sum < target) {
                    j++;
                } else {
                    k--;
                }
            }
        }

        return c;
    }
};

//{ Driver Code Starts.

vector<int> lineArray() {
    string line;
    getline(cin, line);
    stringstream ss(line);
    vector<int> arr;
    int num;
    while (ss >> num) {
        arr.push_back(num);
    }
    return arr;
}

int main() {
    int t;
    cin >> t;
    cin.ignore();
    while (t--) {
        vector<int> arr = lineArray();
        int target;
        cin >> target;
        cin.ignore();

        Solution ob;
        int res = ob.countTriplets(arr, target);
        cout << res << endl;
        cout << "~" << endl;
    }
}

// } Driver Code Ends