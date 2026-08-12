class Solution:
    def shortestPath(self, V: int, edges: list[list[int]]) -> list[int]:
        adj = [[] for _ in range(V)]
        
        for u,v,wt in edges:
            adj[u].append((v,wt))
            
        topoSort = []
        visited = [0]*V
        
        def dfs(node):
            visited[node] = 1
            
            for nv, _ in adj[node]:
                if not visited[nv]:
                    dfs(nv)
                    
            topoSort.append(node)
            
        for v in range(V):
            if not visited[v]:
                dfs(v)
        
        for i in range(V//2):
            topoSort[i], topoSort[V-i-1] = topoSort[V-i-1], topoSort[i]
        
        res = [float('inf')]*V
        res[0] = 0
        
        for node in topoSort:
            for nv, wt in adj[node]:
                currDist = res[node] + wt
                if currDist < res[nv]:
                    res[nv] = currDist
        
        for i in range(V):
            if res[i] == float('inf'):
                res[i] = -1
                
        return res