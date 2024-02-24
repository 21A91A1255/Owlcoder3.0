class Solution {
public:
    #define ll long long
    ll fun(ll n)
    {
        if(n==1) return 0;
        ll a=0,b=0,c=0;
        if(n%2==0)
        {
            c=1+fun(n/2);
        }
        else{
            a=1+fun(n-1);
            b=1+fun(n+1);
            return min(a,b);
        }
        return a+b+c; 
    }
    int integerReplacement(int n) {
        return fun(n);
    }
};