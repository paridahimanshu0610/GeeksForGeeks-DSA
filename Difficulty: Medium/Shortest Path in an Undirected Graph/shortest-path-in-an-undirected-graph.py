import heapq

class Solution:
    def shortestPath(self, V, edges, src, dest):
        adj = [[] for _ in range(V)]
        
        for v1, v2, wt in edges:
            adj[v1-1].append((wt, v2-1))
            adj[v2-1].append((wt, v1-1))
            
        dist = [float("inf")]*V
        dist[src-1] = 0
        track = [None]*V
        
        minHeap = []
        heapq.heappush(minHeap, (0, src-1))
        
        
        def construct_path(node):
            resPath = []
            
            while node is not None:
                resPath.append(node+1)
                node = track[node]
                
            return resPath[::-1]
                
        while len(minHeap) != 0:
            currDist, node = heapq.heappop(minHeap)
            
            if currDist > dist[node]:
                continue
            
            for wt, nv in adj[node]:
                if (currDist+wt) < dist[nv]:
                    dist[nv] = currDist+wt
                    track[nv] = node
                    heapq.heappush(minHeap, (currDist+wt, nv))
                elif (currDist+wt) == dist[nv]:
                    candidate_path = construct_path(node) + [nv+1]
                    current_path = construct_path(track[nv]) + [nv+1]
                    
                    if candidate_path < current_path:
                        track[nv] = node
                        heapq.heappush(minHeap, (currDist+wt, nv))
                    
        res = []
        currNode = dest-1
        
        while currNode is not None:
            res.append(currNode+1)
            currNode = track[currNode]
            
        if dist[dest-1] == float("inf"):
            return [-1]
        else:
            return res[::-1]
            