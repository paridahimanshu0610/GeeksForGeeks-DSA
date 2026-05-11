class Solution:
    def dfs(self, adj, node, stack, visited):
        visited[node] = 1
        
        for e in adj[node]:
            if not visited[e]:
                self.dfs(adj, e, stack, visited)
                
        stack.append(node)
        
    def topoSort(self, v, edges):
        visited = [0]*v
        adj = [[] for _ in range(v)]
        
        for v1, v2 in edges:
            adj[v1].append(v2)
        
        stack = []
        
        for e in range(v):
            if not visited[e]:
                self.dfs(adj, e, stack, visited)
        
        return stack[::-1]