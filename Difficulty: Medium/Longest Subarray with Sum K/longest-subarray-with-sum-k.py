class Solution:
    def longestSubarray(self, a, t):
        sum_map = {0:-1}
        curr_sum, res = 0, 0
        
        for i in range(len(a)):
            curr_sum += a[i]
            
            if curr_sum not in sum_map:
                sum_map[curr_sum] = i
                
            if curr_sum-t in sum_map:
                res = max(res, i - sum_map[curr_sum-t])
                
        return res