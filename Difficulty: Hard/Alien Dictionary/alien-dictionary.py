from collections import defaultdict

class Solution:
    def compare(self, w1, w2, adj):
        n = min(len(w1), len(w2))
        
        for i in range(n):
            c1, c2 = w1[i], w2[i]
            if c1!=c2:
                adj[c1].add(c2)
                return True
        
        # If we complete the for loop without returning True,
        # that means all 'n' starting characters are same.
        # And if len(w1) > len(w2), then alien dictionary is invalid
        
        return len(w1) <= len(w2)
        
    def findOrder(self, words):
        adj = defaultdict(set)
        visited = dict()
        
        for word in words:
            for curr_char in word:
                adj[curr_char]
                visited[curr_char] = 0
        
        for i in range(len(words)-1):
            if not self.compare(words[i], words[i+1], adj):
                return ""
            
        order = []
        
        def dfs(curr):
            visited[curr] = 1
            
            for nv in adj[curr]:
                if not visited[nv]:
                    if not dfs(nv):
                        return False
                elif visited[nv] == 1:
                    return False
                    
            visited[curr] = 2
            order.append(curr)
            
            return True
            
        for c in adj.keys():
            if not visited[c]:
                if not dfs(c):
                    return ""
                    
        return "".join(order[::-1])