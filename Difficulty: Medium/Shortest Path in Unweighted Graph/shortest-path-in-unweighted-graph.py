from collections import deque

class Solution:
    def shortestPath(self, V, edges, src, dest):
        adj = [[] for _ in range(V)]
        
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        q = deque()
        visited = [0]*V
        
        q.appendleft((src, 0))
        visited[src] = 1
        
        while len(q)!=0:
            node, dist = q.pop()
            if node == dest:
                return dist
                
            for nv in adj[node]:
                if not visited[nv]:
                    q.appendleft((nv, dist+1))
                    visited[nv] = 1
                    
        return -1