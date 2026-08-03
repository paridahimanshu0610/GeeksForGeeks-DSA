class Solution:
    def findPos(self, a, x):
        l, h = 0, len(a)-1
        
        while l <= h:
            mid = (l+h)//2
            
            if a[mid] < x:
                l = mid+1
            else:
                h = mid-1
                
        return l
        
    def median(self, a):
        m, n = len(a), len(a[0])
        
        mini, maxi = float("inf"), float("-inf")
        
        for i in range(m):
            mini, maxi = min(mini, a[i][0]), max(maxi, a[i][n-1])
            
        l, h = mini, maxi
        lhs = (m*n)//2
        
        while l <= h:
            mid = (l+h)//2
            total_lhs = 0
            rhs_min = float("inf")
            
            for i in range(m):
                curr_lhs = self.findPos(a[i], mid) # Number of elements on the lhs of mid in a[i]
                total_lhs += curr_lhs 
                curr_rhs_min = a[i][curr_lhs] if curr_lhs < n else float("inf")
                rhs_min = min(rhs_min, curr_rhs_min)
            
            if total_lhs <= lhs:
                l = mid+1
            else:
                h = mid-1
                
        return h