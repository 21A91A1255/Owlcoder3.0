#User function template for Python

class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,s):
        # Code here
        l='1234567890'
        f=1
        if(s[0]=='-'):
            f=-1
            s=s[1:]
        ans=0
        for i in s:
            if i in l:
                ans=ans*10+ord(i)-ord('0')
            else:
                return -1
                
        return f*ans
                
            


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        ob=Solution()
        print(ob.atoi(string))
# } Driver Code Ends