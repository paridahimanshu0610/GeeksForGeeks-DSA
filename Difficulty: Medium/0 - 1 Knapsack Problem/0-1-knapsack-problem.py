class Solution:
    def get_max_val(self, curr_idx, val, wt, curr_capacity, value_so_far):
        if curr_idx==0:
            if wt[0] <= curr_capacity:
                value_so_far[0][curr_capacity] = val[0]
                return value_so_far[0][curr_capacity]
            else:
                return 0
        
        if value_so_far[curr_idx][curr_capacity]!=-1:
            return value_so_far[curr_idx][curr_capacity]
            
        not_pick = self.get_max_val(curr_idx-1,val, wt, curr_capacity, value_so_far)
        pick = float('-inf')
        if wt[curr_idx] <= curr_capacity:
            pick = val[curr_idx] + self.get_max_val(curr_idx-1, val, wt, curr_capacity-wt[curr_idx], value_so_far)
        
        value_so_far[curr_idx][curr_capacity] = max(not_pick, pick)
        
        return value_so_far[curr_idx][curr_capacity]
        
    def knapsack(self, W, val, wt):
        value_so_far = [[0]*(W+1) for i in range(len(val))]
        # self.get_max_val(len(val)-1, val, wt, W, value_so_far)

        for curr_capacity in range(W+1):
            value_so_far[0][curr_capacity] = val[0] if wt[0] <= curr_capacity else 0
        
        for i in range(1, len(val)):
            for curr_capacity in range(W+1):
                not_pick = value_so_far[i-1][curr_capacity]
                pick = float('-inf')
                if wt[i] <= curr_capacity:
                    pick = val[i] + value_so_far[i-1][curr_capacity-wt[i]]
                value_so_far[i][curr_capacity] = max(pick, not_pick)
                
        return value_so_far[len(val)-1][W]