class Solution:
    def maxSubarraySum(self, a):
        currSum, res = 0, float('-inf')
        
        for i in range(len(a)):
            currSum += a[i]
            
            if a[i] > currSum:
                currSum = a[i]
                
            res = max(currSum, res)
        
        return res