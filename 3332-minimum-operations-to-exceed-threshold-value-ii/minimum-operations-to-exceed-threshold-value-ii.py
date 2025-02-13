from queue import PriorityQueue
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        c = 0
        q = PriorityQueue()
        for num in nums:
            q.put(num)
        if q.queue[0] >= k:
            return 0
        while q.qsize() >= 2 and q.queue[0] < k:
            first = q.get()
            second = q.get() 
            new_val = first *2 +  second
            q.put(new_val)
            c += 1
            if q.queue[0] >= k:
                break
        return c
