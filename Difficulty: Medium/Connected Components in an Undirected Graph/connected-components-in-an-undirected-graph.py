class Solution:
    def dfsTraverse(self, adj_list, vertex, components, visited):
        if vertex in visited:
            return components 
        components.append(vertex)
        visited.add(vertex)
        
        for node in adj_list[vertex]:
            if node not in visited: 
                components = self.dfsTraverse(adj_list, node, components, visited)
        return components
        
    def getComponents(self, v, edges):
        adj_list = [[] for _ in range(v)]
        
        for e in edges:
            adj_list[e[0]].append(e[1])
            adj_list[e[1]].append(e[0])
        
        visited = set()
        res = []
        
        for vertex in range(v):
            if vertex not in visited:
                components = self.dfsTraverse(adj_list, vertex, [], visited)
                res.append(components)
            
        return res