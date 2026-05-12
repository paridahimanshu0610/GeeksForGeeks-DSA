import heapq as hq

class Solution:
    def nearlySorted(self, a, k):  
        if len(a) == 1:
            return
        
        temp = [a[i] for i in range(k+1)]
        hq.heapify(temp)
        n = len(a)
        
        for i in range(k+1, n):
            curr_min = hq.heappop(temp)
            a[i-k-1] = curr_min
            hq.heappush(temp, a[i])
            
        
        i = n-k-1
        
        while len(temp) != 0 and i < n:
            curr_min = hq.heappop(temp)
            a[i] = curr_min
            i += 1