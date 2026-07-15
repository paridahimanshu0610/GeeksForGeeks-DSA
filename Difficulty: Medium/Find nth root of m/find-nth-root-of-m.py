class Solution:
    def nthRoot(self, n, m):
        l, h = 0, m
        
        while l <= h:
            mid = (l+h)//2
            
            pow_val = mid**n
            
            if pow_val == m:
                return mid
            elif pow_val < m:
                l = mid+1
            else:
                h = mid-1
        
        return -1