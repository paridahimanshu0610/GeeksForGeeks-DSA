class Solution:
    def soFar(self, a, idx, target, dp):
        if target == 0:
            return True
        elif idx < 0:
            return False
            
        if dp[idx][target] is not None:
            return dp[idx][target]
            
        notTake = self.soFar(a, idx-1, target, dp)
        take = False
        if a[idx] <= target:
            take = self.soFar(a, idx-1, target - a[idx], dp)
            
        dp[idx][target] = (take or notTake)
        
        return dp[idx][target]
        
    def isSubsetSum (self, a, target):
        n = len(a)
        dp = [[None]*(target+1) for _ in range(n)]
        
        return self.soFar(a, n-1, target, dp)