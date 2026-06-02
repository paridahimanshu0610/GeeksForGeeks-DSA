class Solution:
    def soFar(self, wt, val, idx, k, dp):
        if k == 0:
            dp[idx][k] = 0
            return dp[idx][k]
            
        if idx == 0:
            if wt[idx] <= k:
                dp[idx][k] = (k // wt[idx]) * val[idx]
            else:
                dp[idx][k] = 0
                
            return dp[idx][k]
            
        if dp[idx][k] is not None:
            return dp[idx][k]
            
        notTake = self.soFar(wt, val, idx-1, k, dp)
        take = 0
        if wt[idx] <= k:
            take = val[idx] + self.soFar(wt, val, idx, k-wt[idx], dp)
        dp[idx][k] = max(take, notTake)
        
        return dp[idx][k]
            
    def knapSack(self, val, wt, capacity):
        n = len(val)
        dp = [0]*(capacity + 1)
        
        for k in range(capacity + 1):
            if wt[0] <= k:
                dp[k] = (k // wt[0]) * val[0]
                
        for idx in range(1, n):
            temp = [0]*(capacity+1)
            for k in range(capacity+1):
                notTake = dp[k]
                take = 0
                if wt[idx] <= k:
                    take = val[idx] + temp[k-wt[idx]]
                temp[k] = max(take, notTake)                
            dp = temp
            
        return dp[capacity] 