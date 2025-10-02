class Solution:
    def solve(self,i,arr,s,n,ans,res,k):
        if(s==0):
            if(len(ans[:])==k):
                res.append(ans[:])
            return
        if(i==n or s<0):
            return
        ans.append(arr[i])
        self.solve(i+1,arr,s-arr[i],n,ans,res,k)
        ans.pop()
        
        self.solve(i+1,arr,s,n,ans,res,k)
            
    def combinationSum(self, n, k):
        # code here
        ans=[]
        arr=[1,2,3,4,5,6,7,8,9]
        res=[]
        self.solve(0,arr,n,len(arr),ans,res,k)
        return res
        