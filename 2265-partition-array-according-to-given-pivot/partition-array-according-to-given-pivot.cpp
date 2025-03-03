class Solution {
public:
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        vector<int>p,q,r;
        for(int i=0;i<nums.size();i++)
        {
            if(nums[i]<pivot) p.push_back(nums[i]);
            else if(nums[i]>pivot) q.push_back(nums[i]);
            else r.push_back(nums[i]);
        }
        copy(r.begin(), r.end(), back_inserter(p));
        copy(q.begin(), q.end(), back_inserter(p));
        nums.clear();
        for(int i=0;i<p.size();i++)
        {
            nums.push_back(p[i]);
        }
        return nums;
    }
};