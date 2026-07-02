class Solution:
    def leastComp(self, a, l, h, dp):
        if l == h:
            return 0
        
        if dp[l][h] is not None:
            return dp[l][h]
        
        mini = float('inf')   
        for i in range(l, h):
            combination = self.leastComp(a, l, i, dp) + self.leastComp(a, i+1, h, dp)
            currProd = (a[l-1]*a[i]*a[h] + combination)
            mini = min(mini, currProd)
        
        dp[l][h] = mini
        
        return dp[l][h]    
    
    def matrixMultiplication(self, a):
        n = len(a)
        dp = [[0] * n for _ in range(n)]
        
        for length in range(2, n):
            for l in range(1, n-length+1):
                h = l+length-1
                mini = float('inf')
                for i in range(l, h):
                    if l==i:
                        dp[l][i] = 0
                    if i+1 == h:
                        dp[i+1][h] = 0
                        
                    combination = dp[l][i] + dp[i+1][h]
                    currProd = a[l-1]*a[i]*a[h] + combination
                    mini = min(mini, currProd)
                    
                dp[l][h] = mini
        
        return dp[1][n-1]