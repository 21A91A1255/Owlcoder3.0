#User function Template for python3


class Solution:
    def evenlyDivides (self, N):
        # code here
        t=N
        c=0
        while(N>0):
            r=N%10
            if(r!=0):
                if(t%r==0):
                    c+=1
            N=N//10
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends