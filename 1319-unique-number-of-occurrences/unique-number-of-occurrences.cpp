class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        map<int,int>mp;
        set<int>s;
        for(int i=0;i<arr.size();i++)
        {
            mp[arr[i]]++;
        }
        for(auto it: mp)
        {
            cout<<it.second;
            s.insert(it.second);
        }
        if(s.size()==mp.size()) return true;
        return false;
    }
};