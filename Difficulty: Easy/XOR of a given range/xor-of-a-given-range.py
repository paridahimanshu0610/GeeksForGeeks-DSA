class Solution:

    def getXor(self, nums, a, b):
        res = 0
        for i in range(a, b+1):
            res ^= nums[i]
        return res