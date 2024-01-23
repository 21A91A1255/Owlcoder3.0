class Solution {
public:
    void sortColors(vector<int>& nums) {
        map<int,int>mp;
        for(int i=0;i<nums.size();i++)
        {
            mp[nums[i]]++;
        }
        nums.clear();
        for(auto x:mp){
            int k=x.first;
            for(int i=0;i<x.second;i++)
            {
                nums.push_back(k);
            }
        }
    }
};