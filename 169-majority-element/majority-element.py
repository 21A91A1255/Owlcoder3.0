from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=Counter(nums)
        print(c)
        for i in c.keys():
            if(c[i]>len(nums)//2):
                return i

        