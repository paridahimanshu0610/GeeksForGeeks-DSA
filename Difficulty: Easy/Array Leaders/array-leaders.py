class Solution:
    def leaders(self, a):
        greatestSoFar = -float('inf')
        res = []
        
        for i in range(len(a)-1, -1, -1):
            if a[i] >= greatestSoFar:
                res.append(a[i])
            greatestSoFar = max(greatestSoFar, a[i])
        
        return res[::-1]