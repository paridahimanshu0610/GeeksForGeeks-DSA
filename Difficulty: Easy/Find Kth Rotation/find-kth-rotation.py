class Solution:
    def findKRotation(self, a):
        l, h = 0, len(a)-1
        mini, minIdx = float('inf'), -1
        
        while l <= h:
            mid = (l+h)//2
            
            if a[l] <= a[h]:
                if a[l] < mini:
                    mini = a[l]
                    minIdx = l
                break
            
            if a[mid] <= a[h]:
                if a[mid] < mini:
                    mini = a[mid]
                    minIdx = mid
                h = mid-1
            else:
                if a[l] < mini:
                    mini = a[l]
                    minIdx = l
                l = mid+1
                
        return minIdx 