

from typing import List

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums) - 2*k + 1):
            first = nums[i:i+k]
            second = nums[i+k:i+2*k]
            inc1 = True
            for j in range(1, k):
                if first[j] <= first[j-1]:
                    inc1 = False
                    break
            inc2 = True
            for j in range(1, k):
                if second[j] <= second[j-1]:
                    inc2 = False
                    break
            
            if inc1 and inc2:
                return True
        
        return False
