class Solution:
    def soFar(self, a, idx, k, dp):
        if idx == 0:
            if k == 0:
                return 2 if a[idx] == 0 else 1
            else:
                return 1 if a[idx] == k else 0
                
        if (idx, k) in dp:
            return dp[(idx, k)]
            
        take = self.soFar(a, idx-1, k-a[idx], dp)
        notTake = self.soFar(a, idx-1, k, dp)
        
        dp[(idx, k)] = take + notTake
        
        return dp[(idx, k)]
        
    def countSubset(self, a, k):
        n = len(a)
        minSum, maxSum = 0, 0
        for e in a:
            if e >= 0:
                maxSum += e
            else:
                minSum += e
        
        if k > maxSum or k < minSum:
            return 0
            
        dp = [None]*(maxSum-minSum+1)
        
        for target in range(minSum, maxSum+1):
            if target == 0:
                dp[target-minSum] = 2 if a[0] == 0 else 1
            else:
                dp[target-minSum] = 1 if a[0] == target else 0
        
        for idx in range(1, n):
            temp = [None]*(maxSum-minSum+1)
            for target in range(minSum, maxSum+1):
                take = dp[target-a[idx]-minSum] if (0 <= target-a[idx]-minSum < maxSum-minSum+1) else 0
                notTake = dp[target-minSum]
                temp[target-minSum] = take + notTake
            dp = temp
            
        return dp[k-minSum]