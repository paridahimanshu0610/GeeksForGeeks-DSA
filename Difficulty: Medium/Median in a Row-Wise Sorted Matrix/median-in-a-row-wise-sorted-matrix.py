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
            
            for i in range(m):
                # Number of elements strictly less than mid in a[i]
                curr_lhs = self.findPos(a[i], mid)
                total_lhs += curr_lhs
                
            # Consider the list: [1, 3, 5, 17, 25, 29, 33]
            # Now, total_lhs == lhs in 2 scenarios:
            # (mid == 17) or (5 < mid < 17)
            # In the 2nd scenario, we need to move mid towards 17 and so, we should move right by taking l = mid+1.
            # We need to move mid towards 17 because median must be an element from the list (i.e. flattened matrix)
            if total_lhs <= lhs:
                l = mid+1
            else:
                h = mid-1
                
        return h