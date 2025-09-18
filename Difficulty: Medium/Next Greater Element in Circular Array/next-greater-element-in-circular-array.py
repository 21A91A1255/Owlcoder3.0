class Solution:
    def nextGreater(self, arr):
        ans = []
        st = []
        r=arr+arr
        for i in range(len(r) - 1, -1, -1):
            while st and st[-1] <= r[i]:
                st.pop()

            if not st:
                ans.append(-1)
            else:
                ans.append(st[-1])

            st.append(r[i])
        ans=ans[::-1]
        ans=ans[:len(arr)]
        return ans


                