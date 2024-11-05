class Solution:
    def minChanges(self, s: str) -> int:
        #def min_changes_to_make_beautiful(s: str) -> int:
        changes = 0
        
        # Check each pair of characters
        for i in range(0, len(s), 2):
            # Count the number of 1s and 0s in the current pair
            count_0 = 0
            count_1 = 0
            
            # Consider the first character in the pair
            if s[i] == '0':
                count_0 += 1
            else:
                count_1 += 1
                
            # Consider the second character in the pair
            if i + 1 < len(s):
                if s[i + 1] == '0':
                    count_0 += 1
                else:
                    count_1 += 1
            
            # If both are different, we need to change one
            if count_0 == 1 and count_1 == 1:
                changes += 1
        
        return changes
