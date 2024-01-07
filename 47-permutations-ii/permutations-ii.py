from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        k=[]
        p=permutations(nums)
        for i in list(p):
            if list(i) not in k:
                k.append(list(i))
        print(k)
        return k

        