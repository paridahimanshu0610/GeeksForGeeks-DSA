class Solution:
    def findTwoElement(self, a):
        res = []
        
        for e in a:
            idx = (e-1) if e > 0 else (-e-1)
            if a[idx] < 0:
                res.append(idx+1)
            else:
                a[idx] = -a[idx]
        
        for i in range(len(a)):
            if a[i] > 0:
                res.append(i+1)
                
        return res