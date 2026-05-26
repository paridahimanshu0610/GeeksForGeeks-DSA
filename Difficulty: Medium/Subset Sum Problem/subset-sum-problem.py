class Solution:
    def soFar(self, a, idx, target, dp):
        if target == 0:
            dp[idx][target-1] = True
            return dp[idx][target-1]

        if idx == 0:
            dp[idx][target-1] = (a[idx] == target)
            return dp[idx][target-1]

        if dp[idx][target-1] is not None:
            return dp[idx][target-1]

        notTake = self.soFar(a, idx-1, target, dp)
        take = False

        if target >= a[idx]:
            take = self.soFar(a, idx-1, target-a[idx], dp)

        dp[idx][target-1] = (take or notTake)

        return dp[idx][target-1]

    def isSubsetSum (self, a, target):
        n = len(a)
        dp = [[None]*target for _ in range(n)]

        return self.soFar(a, n-1, target, dp)
