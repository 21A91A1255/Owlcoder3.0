#User function Template for python3


class Solution:
    def compareFrac (self, str):
        
        # code here
        t=str.split()
        d=t[0]
        d=d[:-1]
        p=t[1]
        l=[]
        a=''
        for i in range(len(d)):
            if(d[i]!='/'):
                a+=d[i]
            else:
                l.append(int(a))
                a=''
        l.append(int(a))
        v=''
        for i in range(len(p)):
            if(p[i]!='/'):
                v+=p[i]
            else:
                l.append(int(v))
                v=''
        l.append(int(v))
        ans=l[0]/l[1]
        res=l[2]/l[3]
        if(l[0]==0 and l[2]==0):
            return "equal"
        elif(ans>res):
            return d
        elif(ans==res):
            return "equal"
        return p
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import re

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        str = input()
        print(ob.compareFrac(str))

# } Driver Code Ends