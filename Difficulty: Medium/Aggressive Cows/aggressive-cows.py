class Solution:
    def numCowsPlaced(self, a, minDist, k):
        prevPos = a[0]
        cnt = 1
        
        for i in range(1, len(a)):
            if a[i]-prevPos >= minDist:
                prevPos = a[i]
                cnt += 1
            
            if cnt == k:
                return k
                
        return cnt
        
    def aggressiveCows(self, a, k):
        a.sort()
        l, h = 1, max(a)-min(a)
        
        while l <= h:
            mid = (l+h)//2
            totalPlaced = self.numCowsPlaced(a, mid, k)
            
            if totalPlaced < k:
                h = mid-1
            elif totalPlaced >= k:
                l = mid+1
                
        return h