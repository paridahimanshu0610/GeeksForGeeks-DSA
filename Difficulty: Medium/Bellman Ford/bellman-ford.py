class Solution:
    def bellmanFord(self, V: int, edges: list[list[int]], src: int) -> list[int]:
        maxWt = 10**8
        dist = [maxWt]*V
        dist[src] = 0
        
        for _ in range(V-1):
            for u,v,wt in edges:
                if dist[u] == maxWt and dist[v] == maxWt:
                    continue
                
                tempDist = dist[u] + wt
                if tempDist < dist[v]:
                    dist[v] = tempDist
                    
        for u,v,wt in edges:
            if dist[u] == maxWt and dist[v] == maxWt:
                continue

            tempDist = dist[u]+wt
            if tempDist < dist[v]:
                return [-1]
                
        return dist