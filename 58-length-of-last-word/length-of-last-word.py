class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        t=s.split()
        v=t[-1]
        return len(v)
        