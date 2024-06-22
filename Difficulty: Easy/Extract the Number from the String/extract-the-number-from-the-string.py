class Solution:
    def ExtractNumber(self,sentence):
        #code here
        l=[]
        m=0
        s=sentence.split()
        for i in range(len(s)):
            if(s[i].isdigit()):
    
                if '9' not in s[i]:
                    if(int(s[i])>m):
                        m=int(s[i])
        if(m!=0):
            return m
        return -1


#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    S = input()
    ob = Solution()
    ans = ob.ExtractNumber(S)
    print(ans)

# } Driver Code Ends