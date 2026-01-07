class Solution:
    def dfsTraverse(self, adj, node, currList, visited_nodes):
        if node in visited_nodes:
            return currList
            
        visited_nodes.add(node)
        currList.append(node)
        
        for v in adj[node]:
            currList = self.dfsTraverse(adj, v, currList, visited_nodes)
            
        return currList
        
    def dfs(self, adj):
        visited_nodes = set()
        return self.dfsTraverse(adj, 0, [], visited_nodes)