class Solution:
    def searchMatrix(self, mat, x):
        # code here
        p=[]
        for i in range(len(mat)):
            p+=mat[i]
        if x in p:
            return True
        return False