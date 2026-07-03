class Solution:
    def numWaysBoth(self, a, l, h, dp):
        if l == h:
            if a[l] == "T":
                return 1, 0
            else:
                return 0, 1
        
        if dp[l][h] is not None:
            return dp[l][h]
        
        trueCnt, falseCnt = 0, 0
        for i in range(l+1, h):
            if a[i] in {"T", "F"}:
                continue
            
            nTrue1, nFalse1 = self.numWaysBoth(a, l, i-1, dp)
            nTrue2, nFalse2 = self.numWaysBoth(a, i+1, h, dp)
            
            if a[i] == "&":
                trueCnt += nTrue1 * nTrue2
                falseCnt += (nFalse1 * nFalse2 + nTrue1 * nFalse2 + nFalse1 * nTrue2)
            elif a[i] == "|":
                trueCnt += (nTrue1 * nTrue2 + nTrue1 * nFalse2 + nFalse1 * nTrue2)
                falseCnt += nFalse1 * nFalse2
            else:
                trueCnt += (nTrue1 * nFalse2 + nFalse1 * nTrue2)
                falseCnt += nTrue1 * nTrue2 + nFalse1 * nFalse2
        
        dp[l][h] = (trueCnt, falseCnt)
        
        return dp[l][h] 
        
    def countWays(self, a):
        n = len(a)
        dp = [[None]*n for _ in range(n)]
        
        trueCnt, falseCnt = self.numWaysBoth(a, 0, n-1, dp)
        
        return trueCnt