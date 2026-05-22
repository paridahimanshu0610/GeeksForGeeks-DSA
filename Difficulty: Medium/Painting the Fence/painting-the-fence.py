class Solution:
    def soFar(self, idx, k, dp):
        if idx == 0:
            dp[0] = k
            return dp[0]
        elif idx == 1:
            dp[1] = k * k
            return dp[1]
            
        if dp[idx] is not None:
            return dp[idx]
            
        dp[idx] = ((k-1) * self.soFar(idx-1, k, dp)) + ((k-1) * self.soFar(idx-2, k, dp))
        
        return dp[idx]
        
    def countWays(self, n, k):
        dp = [None]*n
        
        return self.soFar(n-1, k, dp)