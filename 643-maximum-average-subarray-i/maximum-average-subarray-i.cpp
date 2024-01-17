class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        long s=0;
        for(int i=0;i<k;i++)
        {
            s+=nums[i];
        }
        long avg_sum=s;
        for(int i=k;i<nums.size();i++)
        {
            avg_sum+=(nums[i]-nums[i-k]);
            s=max(s,avg_sum);
        }
        return s/double(k);
    }
};