class Solution:
	def floydWarshall(self, a):
	    n = len(a[0])
	    maxDist = 10**8
	    
	    for k in range(n):
	        for i in range(n):
	            for j in range(n):
	                if i==k or j==k:
	                    continue
	                
	                if (a[i][j] == maxDist) and (a[i][k] == maxDist or a[k][j] == maxDist):
	                    continue
	                
	                tempDist = a[i][k] + a[k][j]
	                
	                if tempDist < a[i][j]:
	                    a[i][j] = tempDist
	                    
	    return a