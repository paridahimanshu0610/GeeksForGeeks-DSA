import heapq

class Solution:
    def shortestPath(self, V, edges, src, dest):
        adj = [[] for _ in range(V)]
        
        for u,v,wt in edges:
            adj[v-1].append((u-1,wt))
            adj[u-1].append((v-1,wt))
            
        track = [None]*V
        minDist = [float('inf')]*V
        minHeap = []
        res = []
        
        heapq.heappush(minHeap, (0, src-1))
        minDist[src-1] = 0
        
        def constructPath(currNode):
            tempPath = []
            
            while currNode is not None:
                tempPath.append(currNode)
                currNode = track[currNode]
                
            return tempPath[::-1]
        
        while len(minHeap) != 0:
            dist, node = heapq.heappop(minHeap)
            
            if dist > minDist[node]:
                continue
            
            for nv,wt in adj[node]:
                if dist+wt < minDist[nv]:
                    minDist[nv] = dist+wt
                    heapq.heappush(minHeap, (dist+wt, nv))
                    track[nv] = node
                elif dist+wt == minDist[nv]:
                    currentPath = constructPath(nv)
                    candidatePath = constructPath(node)+[nv]
                    
                    if candidatePath < currentPath:  
                        heapq.heappush(minHeap, (dist+wt, nv))
                        track[nv] = node
        
        if track[dest-1] is None and dest!=src:
            return [-1]
        
        currNode = dest-1
        while currNode is not None:
            res.append(currNode+1)
            currNode = track[currNode]
            
        return res[::-1]