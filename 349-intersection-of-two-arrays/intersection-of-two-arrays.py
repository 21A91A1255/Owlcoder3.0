class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
        nums1=set(nums1)
        nums1=list(nums1)
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                l.append(nums1[i])
        return l     