class Solution:
    def minSum(self, arr):
        arr.sort()
        p = []
        q = []
        for i in range(len(arr)):
            if i % 2 == 0:
                p.append(str(arr[i]))
            else:
                q.append(str(arr[i]))
        return self.addStrings(''.join(p), ''.join(q)).lstrip('0') or '0'

    def addStrings(self, num1, num2):
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        res = []
        while i >= 0 or j >= 0 or carry:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            total = n1 + n2 + carry
            res.append(str(total % 10))
            carry = total // 10
            i -= 1
            j -= 1
        return ''.join(res[::-1])
