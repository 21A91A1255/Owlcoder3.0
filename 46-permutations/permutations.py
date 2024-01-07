from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        l=[]
        p=permutations(nums)
        for i in list(p):
            l.append(list(i))
        return l