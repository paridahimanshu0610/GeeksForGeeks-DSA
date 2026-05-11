from collections import deque

class Solution:
    def bfs(self, adj):
        visited = set()
        dq = deque()
        dq.appendleft(0)
        res = [0]
        visited.add(0)
        
        while len(dq) != 0:
            curr = dq.pop()
            
            for e in adj[curr]:
                if e not in visited:
                    visited.add(e)
                    dq.appendleft(e)
                    res.append(e)
        
        return res