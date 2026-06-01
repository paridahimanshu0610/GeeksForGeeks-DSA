class Solution:
    def soFar(self, a, idx, target, dp):
        if idx == 0:
            if a[idx] == 0 and target == 0:
                dp[idx][target] = 2
            elif target == 0:
                dp[idx][target] = 1
            elif a[idx] == target:
                dp[idx][target] = 1
            else:
                dp[idx][target] = 0
            
            return dp[idx][target]

        if target == 0:
            if a[idx] == 0:
                dp[idx][target] = 2
            else:
                dp[idx][target] = 1
                
            return dp[idx][target]
            
        if dp[idx][target] is not None:
            return dp[idx][target]
        
        take = 0
        if a[idx] <= target:
            take = self.soFar(a, idx-1, target-a[idx], dp)
        notTake = self.soFar(a, idx-1, target, dp)
        
        dp[idx][target] = (take + notTake)
        
        return dp[idx][target]
        
    def countPartitions(self, a, diff):
        total = sum(a)
        target = total // 2
        n = len(a)
        
        dp = [0]*(target+1)
        
        # Target == 0
        dp[0] = 2 if a[0] == 0 else 1 
        
        # Target > 0
        if target > 0 and a[0] > 0 and a[0] <= target:
            dp[a[0]] = 1
        
        for idx in range(1, n):
            temp = [None]*(target+1)
            for k in range(target+1):
                take = 0
                if a[idx] <= k:
                    take = dp[k-a[idx]]
                notTake = dp[k]
                temp[k] = (take + notTake)
                
            dp = temp
        
        # print(dp)
        
        cnt = 0        
        for k in range(target+1):
            if dp[k]:
                subset1, subset2 = k, total-k
                if abs(subset1-subset2) == diff:
                    cnt += dp[k]
                    
        return cnt