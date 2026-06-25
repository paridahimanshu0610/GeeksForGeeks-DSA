class Solution:
    def findFloor(self, a, target):
        n = len(a)
        l, h = 0, n-1
        
        while l <= h:
            mid = (l+h)//2
            if target >= a[mid]:
                l = mid+1
            else:
                h = mid-1
                
        return h