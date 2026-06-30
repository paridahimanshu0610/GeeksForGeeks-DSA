class Solution:
    def countFreq(self, a, x):
        lb, rb = None, None
        
        l, h = 0, len(a)-1
        while l <= h:
            mid = (l+h) // 2
            
            if a[mid] >= x:
                h = mid-1
            else:
                l = mid+1
            
        if l < len(a) and a[l] == x:
            lb = l
        else:
            return 0
        
        l, h = 0, len(a)-1    
        while l <= h:
            mid = (l+h) // 2
            
            if a[mid] <= x:
                l = mid+1
            else:
                h = mid-1
                
        if h >= 0 and a[h] == x:
            rb = h
        else:
            return 0
         
        return (rb - lb + 1)
        