class Solution {
public:
    vector<int>x;
    vector<int>p;
    void sort(map<int,int>&mpp)
    {
        multimap<int,int>m;
        for(auto& it:mpp)
        {
            m.insert({it.second,it.first});
        }
        for(auto i:m)
        {
            x.push_back(i.first);
            p.push_back(i.second);
        }
    }
    int findLeastNumOfUniqueInts(vector<int>& arr, int k) {
        map<int,int>mpp;
        for(int i=0;i<arr.size();i++)
        {
            mpp[arr[i]]++;
        }
        sort(mpp);
        int len=p.size();
        for(int i=0;i<x.size();i++)
        {
            if(x[i]<=k)
            {
                k=k-x[i];
                len=len-1;
            }
            else{
                return len;
            }
        }
        return 0;
    }
};