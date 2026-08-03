from collections import deque

class Solution:
    def shortestPath(self, V: int, edges: list[list[int]]) -> list[int]:
        adj = [[] for _ in range(V)]
        
        for u,v,wt in edges:
            adj[u].append((v, wt))
        
        stack = []
        visited = [0]*V
        
        def dfs(curr):
            visited[curr] = 1
            
            for nv, _ in adj[curr]:
                if not visited[nv]:
                    dfs(nv)
                    
            stack.append(curr)
            
        for i in range(V):
            if not visited[i]:
                dfs(i)
        
        dist = [float("inf")]*V
        dist[0] = 0
        
        while len(stack)!=0:
            curr = stack.pop()
            for nv, wt in adj[curr]:
                dist[nv] = min(dist[nv], dist[curr] + wt)
              
        return [-1 if e==float("inf") else e for e in dist]