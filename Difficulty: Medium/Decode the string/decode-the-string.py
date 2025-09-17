class Solution:
    def decodedString(self, s):
        stack = []

        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                word = ""
                while stack and stack[-1] != '[':
                    word = stack.pop() + word
                stack.pop()  

                d = ""
                while stack and stack[-1].isdigit():
                    d = stack.pop() + d
                k = int(d)

                ans = word * k
                for ch in ans:
                    stack.append(ch)

        fs = ""
        while stack:
            fs = stack.pop() + fs
        return fs
