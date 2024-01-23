class Solution:
    def sublists(self,arr,index=0,current=[]):
        m=0
        if(index==len(arr)):
            p=''.join(current)
            if(len(set(p))==len(p)):
                return len(p)
            else:
                return 0
        return max(self.sublists(arr,index+1,current),self.sublists(arr,index+1,current+[arr[index]]))

    def maxLength(self, arr: List[str]) -> int:
        d=self.sublists(arr)
        return d