#User function Template for python3
class Solution:
    def subarraySum(self, a, t):
        l, r = 0, 0
        curr_sum = 0

        while l <= r and r < len(a):
            curr_sum += a[r]

            while curr_sum > t and l <= r:
                curr_sum -= a[l]
                l += 1
            
            if curr_sum == t and l <= r:
                return [l+1, r+1]
            
            r += 1

        return [-1]
