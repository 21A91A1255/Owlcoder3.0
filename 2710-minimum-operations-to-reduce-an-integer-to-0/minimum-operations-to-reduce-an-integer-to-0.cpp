class Solution {
public:
    int minOperations(int n) {
        int c=1;
        queue<long>q;
        q.push(n);
        while(!q.empty())
        {
            long n=q.front();
            if((n&(n-1))==0) return c;
            long l=ceil(log2(n))-1;
            long r=ceil(log2(n));
            l=(1<<l);
            r=(1<<r);
            q.pop();
            if((n-l)<(r-n))
            {
                q.push(n-l);
            }
            else
            {
                q.push(r-n);
            }
            c+=1;
        }
        return -1;
    }
};