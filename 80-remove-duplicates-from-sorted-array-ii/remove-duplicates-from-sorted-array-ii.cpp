class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        map<int,int>mpp;
        int c=0;
        for(int i=0;i<nums.size();i++)
        {
            if(mpp[nums[i]]++>=2)
            {
                c+=1;
                nums[i]=100001;
            }
        }
        sort(nums.begin(),nums.end());
        return nums.size()-c;
    }
};