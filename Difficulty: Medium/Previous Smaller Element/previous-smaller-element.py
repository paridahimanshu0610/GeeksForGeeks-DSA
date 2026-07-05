class Solution:
	def prevSmaller(self, a):
	    n = len(a)
	    res = [None]*n
	    stack = []
	    
	    for i in range(n-1, -1, -1):
	        if len(stack)==0 or a[i] >= a[stack[-1]]:
	            stack.append(i)
	        else:
	            while len(stack) != 0 and a[stack[-1]] > a[i]:
	                res[stack[-1]] = a[i]
	                stack.pop()
	            stack.append(i)
	   
	    while len(stack) > 0:
	        res[stack[-1]] = -1
	        stack.pop()
	       
	    return res