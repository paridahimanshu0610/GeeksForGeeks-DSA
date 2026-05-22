#User function Template for python3

class Solution:
    def soFar(self, a, idx, nextColor, dp):
        if idx == 0:
            if nextColor == 0:
                currCost = min(a[0][1], a[0][2])
            elif nextColor == 1:
                currCost = min(a[0][0], a[0][2])
            elif nextColor == 2:
                currCost = min(a[0][0], a[0][1])
            else:
                currCost = min(a[0])
            dp[0][nextColor] = currCost

            return currCost

        if dp[idx][nextColor] is not None:
            return dp[idx][nextColor]

        if nextColor == 0:
            currCost = min(a[idx][1] + self.soFar(a, idx-1, 1, dp), a[idx][2] + self.soFar(a, idx-1, 2, dp))
        elif nextColor == 1:
            currCost = min(a[idx][0] + self.soFar(a, idx-1, 0, dp), a[idx][2] + self.soFar(a, idx-1, 2, dp))
        elif nextColor == 2:
            currCost = min(a[idx][0] + self.soFar(a, idx-1, 0, dp), a[idx][1] + self.soFar(a, idx-1, 1, dp))
        else:
            currCost = min(a[idx][0] + self.soFar(a, idx-1, 0, dp), a[idx][1] + self.soFar(a, idx-1, 1, dp),  a[idx][2] + self.soFar(a, idx-1, 2, dp))
        
        dp[idx][nextColor] = currCost

        return currCost 
        
    def distinctColoring (self, n, r, g, b):
        a = [None]*n
        i = 0
        for p, q, r in zip(r, g, b):
            a[i] = [p, q, r]
            i += 1
            
        # dp = [[None]*4 for _ in range(len(a))]
        # self.soFar(a, n-1, 3, dp)
        
        if n == 1:
            return min(a[0])
            
        dp = [min(a[0][1], a[0][2]), min(a[0][0], a[0][2]), min(a[0][0], a[0][1])]
        
        for i in range(1, n):
            temp = [None]*3
            for nextColor in range(3):
                if nextColor == 0:
                    temp[nextColor] = min(a[i][1] + dp[1], a[i][2] + dp[2])
                elif nextColor == 1:
                    temp[nextColor] = min(a[i][0] + dp[0], a[i][2] + dp[2])
                elif nextColor == 2:
                    temp[nextColor] = min(a[i][0] + dp[0], a[i][1] + dp[1])
                # else:
                #     temp[nextColor] = min(a[i][0] + dp[0], a[i][1] + dp[1], a[i][2] + dp[2])
                
            dp = temp
                    
        return min(dp)
        
        