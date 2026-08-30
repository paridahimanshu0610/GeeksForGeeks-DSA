import heapq

class Solution:
    def spanningTree(self, V: int, edges: list[list[int]]) -> int:
        minHeap = []
        heapq.heappush(minHeap, (0,0,-1))
        adj = [[] for _ in range(V)]
        for u,v,wt in edges:
            adj[u].append((v,wt))
            adj[v].append((u,wt))
        visited = [0]*V
        res = 0
        mst = []
        
        while len(minHeap)!=0:
            wt,node,parent = heapq.heappop(minHeap)
            
            if visited[node]:
                continue
            
            visited[node] = 1
            if parent!=-1:
                mst.append((parent,node))
                res += wt
            
            for nv,wt in adj[node]:
                if not visited[nv]:
                    heapq.heappush(minHeap, (wt,nv,node))
        
        return res            