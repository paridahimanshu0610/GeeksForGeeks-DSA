import heapq

class Solution:
    def spanningTree(self, V: int, edges: list[list[int]]) -> int:
        minHeap = []
        visited = [0]*V
        adj = [[] for _ in range(V)]
        for u,v,w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))
        
        heapq.heappush(minHeap, (0,0,-1))
        res = 0
        mst_edges = []
        
        while len(minHeap)!=0:
            wt,node,parent = heapq.heappop(minHeap)
            
            if visited[node]:
                continue
            
            visited[node] = 1
            
            if wt!=-1:
                res += wt
                mst_edges.append((parent,node))
                
            for nv,wt in adj[node]:
                if not visited[nv]:
                    heapq.heappush(minHeap, (wt,nv,node))
                    
        return res