class Solution:
    def currBlock(self, a, l, h, dp):
        # if h - l == 2:
        #     dp[l][h] = a[h] * a[h-1] * a[l]
        #     return dp[l][h]
        # elif h - l < 2:
        #     dp[l][h] = 0
        #     return dp[l][h]
        if h == l:
            dp[l][h] = 0
            return 0
        
        if dp[l][h] is not None:
            return dp[l][h]
        
        mini = float('inf')
        for i in range(l, h):
            partition = self.currBlock(a, l, i, dp) + self.currBlock(a, i+1, h, dp)
            curr_prod = a[l-1] * a[i] * a[h]
            mini = min(mini, curr_prod + partition)
            
        dp[l][h] = mini
        
        return dp[l][h]
        
    def matrixMultiplication(self, a):
        n = len(a)
        dp = [[None]*n for _ in range(n)]
        
        return self.currBlock(a, 1, n-1, dp)