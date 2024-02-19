#User function Template for python3
from collections import Counter,OrderedDict
class Solution:
    def minValue(self, s, k):
        # code here
        c=Counter(s)
        m=[]
        y=OrderedDict(c.most_common())
        for i in y.keys():
            m.append(y[i])
        p=[]
        d=0
        while(d!=k):
            m[0]-=1
            d+=1
            m=sorted(m)
            m.reverse()
        ans=0
        for i in range(len(m)):
            ans+=m[i]*m[i]
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        k = int(input())
        
        ob = Solution()
        print(ob.minValue(s, k))
# } Driver Code Ends