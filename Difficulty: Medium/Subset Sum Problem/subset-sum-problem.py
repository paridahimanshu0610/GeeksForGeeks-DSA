class Solution:
    def check(self, a, target, idx, dp):
        if target == 0:
            return True

        if idx == 0:
            dp[target - 1][idx] = (target == a[idx])
            return dp[target - 1][idx]

        if dp[target - 1][idx] is not None:
            return dp[target - 1][idx]

        take = False
        if target >= a[idx]:
            take = self.check(a, target - a[idx], idx - 1, dp)

        not_take = self.check(a, target, idx - 1, dp)

        dp[target - 1][idx] = take or not_take

        return dp[target - 1][idx]

    def isSubsetSum(self, a, target):
        dp = [[None] * len(a) for _ in range(target)]

        return self.check(a, target, len(a) - 1, dp)