class Solution:
    def maxWater(self, arr):
        i = 0
        j = len(arr)-1
        max_area = 0
        while(i<j):
            height = min(arr[i], arr[j])
            width = j-i
            area = height * width
            max_area = max(max_area, area)
            if(arr[i]<arr[j]):
                i+=1
            else:
                j-=1
        return max_area
