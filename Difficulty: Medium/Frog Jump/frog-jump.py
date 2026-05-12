class Solution:
    def minCost(self, a):
        n = len(a)
        if n == 1:
            return 0
            
        dp = [0]*n
        dp[1] = abs(a[1]-a[0])
        
        for i in range(2, n):
            dp[i] = min(dp[i-1] + abs(a[i]-a[i-1]), dp[i-2] + abs(a[i]-a[i-2]))
            
        return dp[n-1]