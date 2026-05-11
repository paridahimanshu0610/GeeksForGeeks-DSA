class Solution:
    def traverse(self, node, adj, visited, res):
        res.append(node)
        visited.add(node)
        
        for e in adj[node]:
            if e not in visited:
                self.traverse(e, adj, visited, res)
            
    def dfs(self, adj):
        visited = set()
        res = []
        self.traverse(0, adj, visited, res)
        
        return res 
        