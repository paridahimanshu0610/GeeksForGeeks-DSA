class Solution:
    def traverse(self, adj, node, curr, visited):
        visited[node] = 1
        curr.append(node)
        
        for e in adj[node]:
            if not visited[e]:
                self.traverse(adj, e, curr, visited)
                
        return curr
        
    def getComponents(self, v, edges):
        res = []
        visited = [0]*v
        
        adj = [[] for _ in range(v)]
        
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
            
        for i in range(v):
            if not visited[i]:
                temp = self.traverse(adj, i, [], visited)
                res.append(temp)
                
        return res