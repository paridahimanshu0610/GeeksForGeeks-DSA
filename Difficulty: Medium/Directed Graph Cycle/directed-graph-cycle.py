class Solution:
    def dfsTraverse(self, a, v, visited):
        visited[v] = 1
        
        for nv in a[v]:
            if not visited[nv]:
                if self.dfsTraverse(a, nv, visited):
                    return True
            elif visited[nv] == 1:
                return True
                
        visited[v] = 2
        
        return False
        
    def isCyclic(self, V, edges):
        a = [[] for _ in range(V)]
        
        for u, v in edges:
            a[u].append(v)
            
        visited = [0]*V
        
        
        for v in range(V):
            if self.dfsTraverse(a, v, visited):
                return True
                
        return False