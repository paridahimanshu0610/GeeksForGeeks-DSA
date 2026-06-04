class Solution:
    def subarrayXor(self, arr, k):
        xor_set = {0: 1}
        curr_xor = 0 
        res = 0
        
        for e in arr:
            curr_xor ^= e
            temp = curr_xor^k
            if temp in xor_set:
                res += xor_set[temp]
            xor_set[curr_xor] = xor_set.get(curr_xor, 0) + 1
        
        return res