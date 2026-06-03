class Solution:
    def soFar(self, s1, s2, idx1, idx2, dp):
        if idx1 < 0 or idx2 < 0:
            return 0
        
        if dp[idx1][idx2] is not None:
            return dp[idx1][idx2]
            
        if s1[idx1] == s2[idx2]:
            prevLen = self.soFar(s1, s2, idx1-1, idx2-1, dp)
            if idx1-1 >= 0 and idx2-1 >= 0 and (s1[idx1-1] == s2[idx2-1]):
                res = 1 + prevLen
            else:
                res = 1
        else:
            res = max(self.soFar(s1, s2, idx1, idx2-1, dp), self.soFar(s1, s2, idx1-1, idx2, dp))
            
        dp[idx1][idx2] = res
        
        return dp[idx1][idx2] 
    
    def longCommSubstr(self, s1, s2):
        m, n = len(s1), len(s2)
        dp = [0]*n
        res = 0
        
        idx2 = 0
        while idx2 < n:
            if s1[0] == s2[idx2]:
                dp[idx2] = 1
                res = max(res, 1)
            idx2 += 1
        
        for idx1 in range(1, m):
            temp = [0]*n
            for idx2 in range(n):
                if s1[idx1] == s2[idx2]:
                    temp[idx2] = (1 + dp[idx2-1]) if idx2-1 >= 0 else 1
                else:
                    temp[idx2] = 0
    
                res = max(res, temp[idx2])
            dp = temp
            
        return res