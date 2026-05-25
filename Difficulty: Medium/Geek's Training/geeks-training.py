class Solution:
    def soFar(self, a, currDay, nextDayActivity, dp):
        if currDay == 0:
            
            maxi = -float('inf')
            for i in range(3):
                if i != nextDayActivity:
                    maxi = max(maxi, a[currDay][i])
            dp[currDay][nextDayActivity] = maxi
            
            return maxi
        
        if dp[currDay][nextDayActivity] is not None:
            return dp[currDay][nextDayActivity]
        
        maxi = -float('inf')
        for i in range(3):
            if i != nextDayActivity:
                maxi = max(maxi, a[currDay][i] + self.soFar(a, currDay-1, i, dp))
        
        dp[currDay][nextDayActivity] = maxi
        
        return maxi
            
    def maximumPoints(self, a):
        n = len(a)
        dp = [[None]*4 for _ in range(n)]
        
        return self.soFar(a, n-1, 3, dp)