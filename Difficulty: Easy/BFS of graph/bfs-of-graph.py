from collections import deque

class Solution:
    def bfs(self, a):
        q = deque()
        visited = [0]*len(a)
        res = []
        
        q.appendleft(0)
        res.append(0)
        visited[0] = 1
        
        while len(q) != 0:
            curr = q.pop()
            
            for e in a[curr]:
                if not visited[e]:
                    q.appendleft(e)
                    res.append(e)
                    visited[e] = 1
        
        return res