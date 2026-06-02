#User function Template for python3

class Solution:
    def soFar(self, a, idx, currLen, dp):
        if currLen == 0:
            dp[idx][currLen] = 0
            return dp[idx][currLen]
        
        if idx == 0:
            dp[idx][currLen] = a[currLen-1]
            return dp[idx][currLen] 
        
        if dp[idx][currLen] is not None:
            return dp[idx][currLen]
            
        sellPieceLen = currLen-idx
        
        cut = 0
        if sellPieceLen >= 1:
            cut = a[sellPieceLen-1] + self.soFar(a, idx-1, currLen - sellPieceLen, dp)
        notCut = self.soFar(a, idx-1, currLen, dp)
        
        dp[idx][currLen] = max(cut, notCut)
        
        return dp[idx][currLen]
        
    def cutRod(self, a):
        n = len(a)
        
        dp = [0]*(n+1)
        for currLen in range(1, n+1):
            dp[currLen] = a[currLen-1]
        
        for idx in range(1, n):
            temp = [0]*(n+1)
            for currLen in range(1, n+1):
                sellPieceLen = currLen-idx
                cut = 0
                if sellPieceLen >= 1:
                    cut = a[sellPieceLen-1] + dp[currLen - sellPieceLen]
                notCut = dp[currLen]
                
                temp[currLen] = max(cut, notCut)                
            dp = temp
            
        return dp[n]