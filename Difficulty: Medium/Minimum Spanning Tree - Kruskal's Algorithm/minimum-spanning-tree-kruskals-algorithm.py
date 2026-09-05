from typing import List

class Solution:
    def kruskalsMST(self, V: int, edges: List[List[int]]) -> int:
        size = [1]*V
        parent = [i for i in range(V)]
        
        def findUltimateParent(node):
            if node == parent[node]:
                return node
            
            parent[node] = findUltimateParent(parent[node])
            
            return parent[node]
        
        def haveSameUltimateParent(u, v):
            return findUltimateParent(u) == findUltimateParent(v)
            
        def unionBySize(u, v):
            pu, pv = findUltimateParent(u), findUltimateParent(v)
            
            if size[pu] < size[pv]:
                parent[pu] = pv
                size[pv] += size[pu]
            else:
                parent[pv] = pu
                size[pu] += size[pv]
        
        edges.sort(key = lambda x: x[-1])
        mst_edges = []
        res = 0
        
        for u,v,wt in edges:
            if haveSameUltimateParent(u,v):
                continue
            
            res += wt
            mst_edges.append((u,v))
            
            unionBySize(u,v)
            
        return res