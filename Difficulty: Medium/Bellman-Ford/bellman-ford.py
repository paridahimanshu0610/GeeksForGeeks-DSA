#User function Template for python3

class Solution:
    def bellmanFord(self, v, edges, src):
        max_dist = 10**8 
        dist = [max_dist]*v
        dist[src] = 0
        
        changed = False
        
        for i in range(v):
            for v1, v2, d in edges:
                if (dist[v1] != max_dist) and ((dist[v1] + d) < dist[v2]):
                    dist[v2] = dist[v1] + d
                    changed = True
            
            if changed == False:
                break
        
        for v1, v2, d in edges:
            if (dist[v1] != max_dist) and ((dist[v1] + d) < dist[v2]):
                return [-1]
            
        return dist