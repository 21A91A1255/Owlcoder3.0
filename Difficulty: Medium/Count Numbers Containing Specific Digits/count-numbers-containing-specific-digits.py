class Solution:
    def countValid(self, n, arr):
        allowed_digits = set(arr)
        all_digits = set(range(10))
        other_digits = list(all_digits - allowed_digits)
    
        total = 9 * (10 ** (n - 1))
    
      
        if not other_digits:
            return total
    
        B = other_digits
        b = len(B)
    
        count = 0
        for i in range(b):
            if B[i] == 0:
                continue
            curr = 1
            for j in range(1, n):
                curr *= b
            count += curr
    
        return total - count
