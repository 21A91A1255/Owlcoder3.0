class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        p=sorted(heights)
        h=p[::-1]
        l=[]
        for i in range(len(h)):
            k=heights.index(h[i])
            l.append(names[k])
        return l
