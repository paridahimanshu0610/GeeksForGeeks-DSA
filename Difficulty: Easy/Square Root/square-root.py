class Solution:
    def floorSqrt(self, n):
        l, h = 1, n
        
        while l <= h:
            mid = (l+h)//2
            
            square = mid**2
            
            if square > n:
                h = mid-1
            elif square < n:
                l = mid+1
            else:
                return mid
                
        return h