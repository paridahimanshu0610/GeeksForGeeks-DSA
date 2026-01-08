from collections import deque
class Solution:
    def dfs(self, adj_list, vertex, stack, visited):
        if visited[vertex]==1:
            return
        
        visited[vertex] = 1
        
        for node in adj_list[vertex]:
            if visited[node]==0:
                self.dfs(adj_list, node, stack, visited)
                
        stack.append(vertex)
            
    def topoSort(self, v, edges):
        visited = [0]*v
        stack = deque()
        adj_list = [[] for _ in range(v)]
        
        for e in edges:
            adj_list[e[0]].append(e[1])
        
        for vertex in range(v):
            if visited[vertex]==0:
                self.dfs(adj_list, vertex, stack, visited)
        
        # print(stack)
        res = []
        while len(stack)!=0:
            temp = stack.pop()
            # print(temp)
            res.append(temp)
        # print(res)
        
        return res