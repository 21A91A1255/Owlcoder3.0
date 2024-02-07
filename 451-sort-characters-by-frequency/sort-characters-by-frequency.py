from collections import Counter,OrderedDict
class Solution:
    def frequencySort(self, s: str) -> str:
        c=Counter(s)
        ans=''
        y = OrderedDict(c.most_common())
        for i in y.keys():
            for j in range(y[i]):
                ans+=i
        return ans