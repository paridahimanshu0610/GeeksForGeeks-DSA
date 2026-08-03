class Solution:
    def getOneIdx(self, a):
        n = len(a)
        l, h = 0, n-1
        
        while l <= h:
            mid = (l+h)//2
            
            if a[mid] == 1:
                h = mid-1
            else:
                l = mid+1
                
        return l
        
    def rowWithMax1s(self, a):
        m, n = len(a), len(a[0])
        maxOnes = 0
        res = -1
        
        for i in range(len(a)):
            idx = self.getOneIdx(a[i])
            if (n-idx) > maxOnes:
                maxOnes = n-idx
                res = i
                
        return res