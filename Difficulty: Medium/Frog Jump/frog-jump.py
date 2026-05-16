class Solution:
    def minCost(self, a):
        if len(a) == 1:
            return 0
            
        total_energy = 0
        prev1, prev2 = abs(a[1]-a[0]), 0 
        
        i = 2
        
        while i < len(a):
            curr_step_energy = min(prev1 + abs(a[i]-a[i-1]), prev2 + abs(a[i]-a[i-2]))
            prev1, prev2 = curr_step_energy, prev1
            i += 1
            
        return prev1