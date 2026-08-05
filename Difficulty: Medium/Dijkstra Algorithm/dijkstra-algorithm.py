import heapq

class Solution:
    def dijkstra(self, V: int, edges: list[list[int]], src: int) -> list[int]:
        adj = [[] for _ in range(V)]
        
        for v1, v2, wt in edges:
            adj[v1].append((v2, wt))
            adj[v2].append((v1, wt))
            
        dist = [float("inf")]*V
        dist[src] = 0

        mindist = []
        heapq.heappush(mindist, (0, src))
        
        visited = [0]*V
        while len(mindist)!=0:
            currDist, node = heapq.heappop(mindist)
            
            if visited[node]:
                continue
            visited[node] = 1
            
            for nv, wt in adj[node]:
                if (currDist + wt) < dist[nv]:
                    dist[nv] = currDist + wt
                    heapq.heappush(mindist, (dist[nv], nv))
                        
        return dist