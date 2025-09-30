class Solution:
    def binstr(self, n):
        # code here
        l=2**n
        ans=[]
        m=['0']*n
        for i in range(l):
            b=bin(i)[2:]
            if(len(b)<n):
                a=m[:n-len(b)]
                a.append(b)
                s=''.join(a)
                ans.append(s)
            else:
                ans.append(b)
        return ans