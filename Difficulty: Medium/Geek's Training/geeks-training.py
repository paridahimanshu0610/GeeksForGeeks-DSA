class Solution:
    def compute(self, a, day, last, dp):
        if day == 0:
            maxi = 0
            for i in range(3):
                if i!=last:
                    maxi = max(maxi, a[0][i])
            dp[0][last] = maxi
            return maxi
        
        if dp[day][last] is not None:
            return dp[day][last]
            
        maxi = 0
        for i in range(3):
            if i!=last:
                maxi = max(maxi, self.compute(a, day-1, i, dp) + a[day][i])
        
        dp[day][last] = maxi
        return maxi
            
    def maximumPoints(self, a):
        dp = [[None]*4 for _ in range(len(a))]
        
        return self.compute(a, len(a)-1, 3, dp)