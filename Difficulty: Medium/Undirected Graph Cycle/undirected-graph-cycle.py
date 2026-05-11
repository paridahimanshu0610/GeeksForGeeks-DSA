from collections import deque

class Solution:
    def hasCycle(self, adj, src, visited):
	    dq = deque()
		
		dq.appendleft((src, -1))
		visited[src] = 1
		
		
		while len(dq) != 0:
		    curr_size = len(dq)
		    
		    for _ in range(curr_size):
		        node, parent = dq.pop()
		        
		        for e in adj[node]:
		            if not visited[e]:
		                visited[e] = 1
		                dq.appendleft((e, node))
		            elif visited[e] and e != parent:
		                return True
		 
		return False 
		                
	def isCycle(self, v, edges):
	    adj = [[] for _ in range(v)]
	    visited = [0]*v

	    for v1, v2 in edges:
	        adj[v1].append(v2)
	        adj[v2].append(v1)
	
		for e in range(v):
		    if not visited[e] and self.hasCycle(adj, e, visited):
		        return True
		        
        return False