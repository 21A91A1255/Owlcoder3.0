class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for i in strs:
            k=sorted(i)
            k="".join(k)
            if k not in dic:
                dic[k]=[i]
            else:
                dic[k].append(i)
        return dic.values()
        