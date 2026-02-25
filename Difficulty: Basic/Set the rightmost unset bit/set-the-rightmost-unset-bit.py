#User function Template for python3
class Solution:
	def setBit(self, n):
		temp = n
		shift = 0
		
		while (temp>>shift & 1)!=0:
		    shift += 1
		
		return (1<<shift | n)