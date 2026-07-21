class Solution:
    def topoSort(self, V, edges):
        a = [[] for _ in range(V)]
        
        for u, v in edges:
            a[u].append(v)
        
        res = []
        visited = [0]*V
        
        def dfs(node):
            visited[node] = 1
            
            for idx in a[node]:
                if not visited[idx]:
                    if not dfs(idx):
                        return False
                elif visited[idx] == 1:
                    return False
            
            visited[node] = 2
            res.append(node)
            
            return True
        
        for v in range(V):
            if not visited[v]:
                if not dfs(v):
                    return []
        
        return res[::-1]