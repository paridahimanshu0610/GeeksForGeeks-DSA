class Solution:
    def DSU(self, n, queries):
        adj = [i for i in range(n+1)]
        
        res = []
        def find_root(node):
            if adj[node] == node:
                return node
            
            adj[node] = find_root(adj[node])
            
            return adj[node]

        for query in queries:
            if len(query) == 2:
                res.append(find_root(query[1]))
            else:
                rx = find_root(query[1])
                rz = find_root(query[2])
                adj[rx] = rz
                
        return res