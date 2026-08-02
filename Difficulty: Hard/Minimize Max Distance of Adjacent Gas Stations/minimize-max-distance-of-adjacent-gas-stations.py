import math

class Solution:
    def numPlaced(self, a, dist, k):
        n = len(a)
        cnt = 0
        
        for i in range(1, n):
            gap = a[i]-a[i-1]
            cnt += (math.ceil(gap/dist)-1)
                
        return cnt
            
    def minMaxDist(self, a, k):
        n = len(a)
        l = 10**(-6)
        h = 10**(-6)
        
        for i in range(1, n):
            h = max(h, a[i]-a[i-1])
        
        while (h-l) >= 10**(-6):
            mid = (l+h)/2
            cnt = self.numPlaced(a, mid, k)
            
            if cnt <= k:
                h = mid
            else:
                l = mid
                
        return round(l, 6)