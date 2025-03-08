class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l=[]
        for i in range(len(blocks)+1-k):
            s=blocks[i:k+i]
            l.append(s.count('W'))
        return min(l)