class Solution:
    def dfs(self, adj, node, visited):
        visited[node] = 1
        
        for e in adj[node]:
            if not visited[e]:
                if self.dfs(adj, e, visited):
                    return True
            elif visited[e] == 1:
                return True
                
        visited[node] = 2
        
        return False
        
    def isCyclic(self, v, edges):
        visited = [0]*v
        adj = [[] for _ in range(v)]
        
        for v1, v2 in edges:
            adj[v1].append(v2)
            
        for e in range(v):
            if not visited[e]:
                if self.dfs(adj, e, visited):
                    return True
                    
        return False