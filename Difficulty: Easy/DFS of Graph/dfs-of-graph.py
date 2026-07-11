class Solution:
    def dfsTraverse(self, a, idx, visited, res):
        res.append(idx)
        visited[idx] = 1
        
        for e in a[idx]:
            if not visited[e]:
                self.dfsTraverse(a, e, visited, res)
        
    def dfs(self, a):
        res = []
        visited = [0]*len(a)
        idx = 0
        
        self.dfsTraverse(a, idx, visited, res)
        
        return res