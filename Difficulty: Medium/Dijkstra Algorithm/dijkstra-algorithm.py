import heapq as hq

class Solution:
    def dijkstra(self, v, edges, src):
        adj = [[] for _ in range(v)]
        
        for v1, v2, d in edges:
            adj[v1].append((v2, d))
            adj[v2].append((v1, d))  # reverse edge for undirected graph
        
        dist = [float('inf')] * v
        dist[src] = 0
        
        visited = [0]*v
        dist_heap = []
        hq.heappush(dist_heap, (0, src))
        
        while len(dist_heap) != 0:
            curr_d, curr_node = hq.heappop(dist_heap)
            
            if visited[curr_node]:
                continue
            visited[curr_node] = 1
            
            for node, d in adj[curr_node]:
                if dist[node] > (curr_d + d):
                    dist[node] = curr_d + d
                    hq.heappush(dist_heap, (dist[node], node))
                    
        return dist