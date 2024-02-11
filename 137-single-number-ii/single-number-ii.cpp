class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int res=0;
        for(int i=0;i<32;i++)
        {
            int c=0, x=(1<<i);
            for(int j=0;j<nums.size();j++) if((x&nums[j])!=0) c++;
            if(c%3!=0) res=(x|res);
        }
        return res;
    }
};