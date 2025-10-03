class Solution:
    def fun(self, i, arr, currstr, digits, res):
        if i == len(arr):
            res.append(currstr)
            return
        d = str(arr[i])
        if digits[d] == "": 
            self.fun(i + 1, arr, currstr, digits, res)
        else:
            for c in digits[d]:
                self.fun(i + 1, arr, currstr + c, digits, res)
    def possibleWords(self, arr):
        res = []
        digits = {
            "0":"",
            "1":"",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        self.fun(0, arr, "", digits, res)
        return res
