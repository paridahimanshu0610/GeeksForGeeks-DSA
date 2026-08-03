class Solution:
    def kthElement(self, a1, a2, k):
        n, m = len(a1), len(a2)
        if n > m:
            return self.kthElement(a2, a1, k)
            
        l, h = 0, min(n, k)
        
        while l <= h:
            mid1 = (l+h)//2
            mid2 = k-mid1
            
            if mid2 > m:
                l = mid1+1
                continue
            
            l1 = a1[mid1-1] if mid1 >= 1 else float("-inf")
            l2 = a2[mid2-1] if mid2 >= 1 else float("-inf")
            
            r1 = a1[mid1] if mid1 < n else float("inf")
            r2 = a2[mid2] if mid2 < m else float("inf")
            
            if l1 > r2:
                h = mid1-1
            elif l2 > r1:
                l = mid1+1
            else:
                break
            
        return max(l1, l2)