class Solution:
    def countGreater(self, a, indices):
        res = [0]*len(indices)
        
        for idx in range(len(indices)):
            cnt = 0
            for i in range(indices[idx]+1, len(a)):
                if a[i] > a[indices[idx]]:
                    res[idx] += 1
                    
        return res