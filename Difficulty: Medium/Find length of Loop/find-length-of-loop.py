class Solution:
    def lengthOfLoop(self, head):
        if head is None or head.next is None:
            return 0
        visited = {}
        pos = 0
        while head is not None:
            if head in visited:
                return pos - visited[head]
            visited[head] = pos
            pos += 1
            head = head.next
        return 0
