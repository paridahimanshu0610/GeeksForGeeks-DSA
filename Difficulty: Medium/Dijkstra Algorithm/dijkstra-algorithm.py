import heapq

class Solution:
    def dijkstra(self, V: int, edges: list[list[int]], src: int) -> list[int]:
        adj = [[] for _ in range(V)]
        
        for u,v,wt in edges:
            adj[u].append((v,wt))
            adj[v].append((u,wt))
            
        minHeap = []
        visited = [0]*V
        res = [float('inf')]*V
        
        res[src] = 0
        heapq.heappush(minHeap, (0, src))
        
        while len(minHeap) != 0:
            dist, node = heapq.heappop(minHeap)
            if visited[node]:
                continue
            visited[node] = 1
             
            for nv,wt in adj[node]:
                if dist+wt < res[nv]:
                    res[nv] = dist+wt
                    heapq.heappush(minHeap, (dist+wt, nv))
                    
        return res