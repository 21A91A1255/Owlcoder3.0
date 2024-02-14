class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        vector<int>p;
        vector<int>m;
        vector<int>ans;
        for(int i=0;i<nums.size();i++)
        {
            if(nums[i]>0)
            {
                p.push_back(nums[i]);
            }
            else
            {
                m.push_back(nums[i]);
            }
        }
        for(int j=0;j<p.size();j++)
        {
            ans.push_back(p[j]);
            ans.push_back(m[j]);
        }
        return ans;
    }
};