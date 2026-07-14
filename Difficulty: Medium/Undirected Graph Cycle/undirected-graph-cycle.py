class Solution:
    def dfsTraverse(self, a, v, visited, parent):
        visited[v] = 1
        
        for nv in a[v]:
            if not visited[nv]:
                if self.dfsTraverse(a, nv, visited, v):
                    return True
            elif visited[nv] and nv != parent:
                return True
                
        return False
        
	def isCycle(self, V, edges):
	    a = [[] for _ in range(V)]
	    
	    for u, v in edges:
	        a[u].append(v)
	        a[v].append(u)
	    
	    visited = [0]*V
	    
	    for v in range(V):
	        parent = None
	        if not visited[v]:
	            if self.dfsTraverse(a, v, visited, parent):
	                return True
	    
	    return False