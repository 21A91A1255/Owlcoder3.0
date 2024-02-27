class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        q=(1<<len(nums))
        p=[]
        for i in range(q):
            k=[]
            for j in range(len(nums)):
                if(i&(1<<j)):
                    k.append(nums[j])
            p.append(k)
        return p
        