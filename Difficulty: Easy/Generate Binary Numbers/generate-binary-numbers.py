class Solution:
    def generateBinary(self, n):
        if n <= 0:
            return []
        q = deque()
        q.append("1")
        res = []
        while len(res) < n:
            s = q.popleft()
            res.append(s)
            q.append(s + "0")
            q.append(s + "1")
        return res
