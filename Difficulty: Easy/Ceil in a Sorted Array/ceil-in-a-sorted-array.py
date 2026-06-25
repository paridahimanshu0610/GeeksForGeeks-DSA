class Solution:
    def findCeil(self, a, x):
        n = len(a)
        l, h = 0, n-1
        
        while l <= h:
            mid = (l+h)//2
            if x <= a[mid]:
                h = mid-1
            else:
                l = mid+1
                
        return l if l < n else -1 