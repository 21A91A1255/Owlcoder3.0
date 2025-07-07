class Solution:
    def nextLargerElement(self, arr):
        ans = []
        st = []

        for i in range(len(arr) - 1, -1, -1):
            while st and st[-1] <= arr[i]:
                st.pop()

            if not st:
                ans.append(-1)
            else:
                ans.append(st[-1])

            st.append(arr[i])

        return ans[::-1]  
