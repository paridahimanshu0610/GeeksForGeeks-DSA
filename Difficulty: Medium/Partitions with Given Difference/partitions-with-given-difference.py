class Solution:
    def soFar(self, a, idx, k, dp):
        if idx == 0:
            if k == 0:
                return 2 if a[idx] == 0 else 1
            else:
                return 1 if a[idx] == k else 0
                
        if (idx, k) in dp:
            return dp[(idx, k)]
            
        take = self.soFar(a, idx-1, k - a[idx], dp)
        notTake = self.soFar(a, idx-1, k, dp)
        
        dp[(idx, k)] = take + notTake
        
        return dp[(idx, k)]
        
    def countPartitions(self, a, diff):
        n = len(a)
        dp = {}
        minSum, maxSum, total = 0, 0, 0
        
        for e in a:
            total += e
            if e > 0:
                maxSum += e
            else:
                minSum += e
                
        dp = [0]*(maxSum-minSum+1)
        
        for k in range(minSum, maxSum+1):
            new_point = k - minSum
            if k == 0:
                dp[new_point] = 2 if a[0] == 0 else 1
            else:
                dp[new_point] = 1 if a[0] == k else 0
                
        for idx in range(1, n):
            temp = [0]*(maxSum-minSum+1)
            for k in range(minSum, maxSum+1):
                # Take
                take = dp[k-a[idx]-minSum] if 0 <= k-a[idx]-minSum < maxSum-minSum+1 else 0
                
                # Not take
                notTake = dp[k - minSum]
                
                temp[k - minSum] = take + notTake
            dp = temp
        
        # print(dp)
        res = 0
        for k in range(minSum, (minSum+maxSum)//2 + 1):
            new_point = k - minSum
            if dp[k] > 0 and abs(total - 2*k) == diff:
                res += dp[k]
        
        return res