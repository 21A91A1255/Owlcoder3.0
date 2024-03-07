#User function Template for python3

class Solution:
    def search(self, p, t):
        # code here
        n=len(t)
        m=len(p)
        l=[]
        for i in range(n-m+1):
            cnt=0
            for j in range(i,i+m):
                if(p[j-i]==t[j]):
                    cnt+=1
                else:
                    break
            if cnt==m:
                l.append(i+1)
        return l


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        for value in ans:
            print(value,end = ' ')
        print()
# } Driver Code Ends