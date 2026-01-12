class Solution:
    def get_max(self, wt, val, W, curr_item, curr_wt, dp):
        if curr_item == 0:
            if curr_wt + wt[0] <= W:
                dp[0][curr_wt] = val[0]
                return dp[0][curr_wt]
            else:
                dp[0][curr_wt] = 0
                return dp[0][curr_wt]
        
        if dp[curr_item][curr_wt]!=-1:
            return dp[curr_item][curr_wt] 
        
        not_pick_value = self.get_max(wt, val, W, curr_item-1, curr_wt, dp)
        
        if curr_wt + wt[curr_item] <= W:
            pick_value = val[curr_item] + self.get_max(wt, val, W, curr_item-1, curr_wt + wt[curr_item], dp)
        else:
            pick_value = not_pick_value
        
        dp[curr_item][curr_wt] = max(not_pick_value, pick_value)
        
        return dp[curr_item][curr_wt] 
        
    def knapsack(self, W, val, wt):
        curr_item, curr_wt = len(val)-1, 0
        dp = [0]*(W+1)
        
        for w in range(W+1):
            dp[w] = val[0] if w + wt[0] <= W else 0
        
        for i in range(1, len(val)):
            for w in range(W+1):
                not_pick = dp[w]
                if w+wt[i] <= W:
                    pick = val[i] + dp[w+wt[i]]
                else:
                    pick = not_pick
                    
                dp[w] = max(pick, not_pick)
        
        # self.get_max(wt, val, W, curr_item, curr_wt, dp)
        return dp[0] 