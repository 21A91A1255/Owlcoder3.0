class Solution:
    def previousSmaller(self, arr):
        st = []
        res = []
        for i in range(len(arr)):
            while st and arr[st[-1]] >= arr[i]:
                st.pop()
            if not st:
                res.append(-1)
            else:
                res.append(st[-1])
            st.append(i)
        return res
    def nextSmaller(self, arr):
        n = len(arr)
        st = []
        res = [len(arr)] * n
        for i in range(n - 1, -1, -1):
            while st and arr[st[-1]] >= arr[i]:
                st.pop()
            if st:
                res[i] = st[-1]
            st.append(i)
        return res

        
    def maxOfMins(self, arr):
        rel1=self.previousSmaller(arr)
        rel2=self.nextSmaller(arr)
        
        ans=[0]*len(arr)
        for i in range(len(rel1)):
            a=(rel2[i]-rel1[i]-1)
            ans[a-1]=max(ans[a-1],arr[i])
            
        for i in range(len(arr) - 2, -1, -1):
            ans[i] = max(ans[i], ans[i + 1])
        return ans
        
            
           