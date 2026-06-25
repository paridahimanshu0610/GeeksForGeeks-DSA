class Solution:
    def lowerBound(self, a, target):
        n = len(a)
        l, h = 0, n-1
        
        while l <= h:
            mid = (l+h)//2
            if target <= a[mid]:
                h = mid-1
            else:
                l = mid+1
        
        return l