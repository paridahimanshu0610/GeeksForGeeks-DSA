class Solution:
    def longestBitonicSequence(self, n : int, a : list[int]) -> int:
        dp1 = [1] * n
        dp2 = [1] * n
        # track1 = [None] * n
        # track2 = [None] * n
        # curr_idx = 0
        
        for idx in range(n):
            for prev_idx in range(idx):
                if (a[idx] > a[prev_idx]) and (1 + dp1[prev_idx] > dp1[idx]):
                    dp1[idx] = 1 + dp1[prev_idx]
                    # track1[idx] = prev_idx
                
        for idx in range(n-1, -1, -1):
            for prev_idx in range(idx+1, n):
                if (a[idx] > a[prev_idx]) and (1 + dp2[prev_idx] > dp2[idx]):
                    dp2[idx] = 1 + dp2[prev_idx]
                    # track2[idx] = prev_idx
        
        # print(dp1, "\n", dp2) 
        maxLen = 0   
        for i in range(n):
            if (dp1[i] > 1) and (dp2[i] > 1) and (dp1[i] + dp2[i] - 1) > maxLen:
                maxLen = dp1[i] + dp2[i] - 1
                # curr_idx = i
            
        return maxLen