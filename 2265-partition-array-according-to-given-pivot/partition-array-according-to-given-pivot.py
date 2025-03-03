class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        p=[]
        r=[]
        q=[]
        for i in range(len(nums)):
            if(nums[i]<pivot):
                p.append(nums[i])
            elif(nums[i]>pivot):
                q.append(nums[i])
            else:
                r.append(nums[i])
        return p+r+q  