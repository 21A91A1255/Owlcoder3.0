class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        p=list(s)
        s.clear()
        for i in range(len(p)-1,-1,-1):
            s.append(p[i])
        return s


        