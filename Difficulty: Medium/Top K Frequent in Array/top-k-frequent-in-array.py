from collections import Counter
class Solution:
	def topKFreq(self, arr, k):
		# Code here
		l=[]
		arr.sort()
		arr.reverse()
		c=Counter(arr)
		p=c.most_common(k)
		for i in range(len(p)):
		    d=p[i]
		    l.append(d[0])
		return l
		
		