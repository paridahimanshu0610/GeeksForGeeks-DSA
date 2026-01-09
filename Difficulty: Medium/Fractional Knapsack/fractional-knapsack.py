class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        temp = [0]*len(val)
        
        for i in range(len(val)):
            temp[i] = (i, val[i]/wt[i])
            
        temp.sort(key=lambda x: x[1], reverse=True)
        res = 0
        curr_cap = capacity
        
        for ii, curr_density in temp:
            if curr_cap==0:
                return res
            
            curr_item_load = wt[ii] if wt[ii] <= curr_cap else curr_cap
            
            res += curr_item_load*curr_density
            curr_cap -= curr_item_load
            

        return round(res, 6)            