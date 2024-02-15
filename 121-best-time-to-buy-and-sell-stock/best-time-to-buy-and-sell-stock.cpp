class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxp=0,l=0,r=1,pro=0;
        while(r<prices.size())
        {
            if(prices[l]<prices[r])
            {
                pro=prices[r]-prices[l];
                maxp=max(maxp,pro);
            }
            else
            {
                l=r;
            }
            r+=1;
        }
        return maxp;
    }
};