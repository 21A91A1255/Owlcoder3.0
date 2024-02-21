class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ans=0
        if(left==right):
            return left
        while(left<right):
            ans=right&(right-1)
            right=ans
            if(ans==0):
                return 0
        return ans