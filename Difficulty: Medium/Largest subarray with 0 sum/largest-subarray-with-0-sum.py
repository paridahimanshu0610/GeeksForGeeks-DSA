class Solution:
    def maxLength(self, a):
        prefixSum = {0: -1}
        currSum = 0
        target = 0
        res = 0
        
        for i in range(len(a)):
            currSum += a[i]
            if (currSum - target) in prefixSum:
                res = max(res, i - prefixSum[(currSum - target)])
            
            if currSum not in prefixSum:
                prefixSum[currSum] = i
                
        return res 