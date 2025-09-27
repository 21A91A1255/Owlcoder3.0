class Solution:
    def kBitFlips(self, arr, k):
        n=len(arr)
        ans=0
        flip=0
        fliparray=[0]*n
        for i in range(len(arr)):
            if(i>=k):
                flip^=fliparray[i-k]
            if(flip==arr[i]):
                if(i+k>n):
                    return -1
                fliparray[i]=1
                flip^=1
                ans+=1
        return ans
                