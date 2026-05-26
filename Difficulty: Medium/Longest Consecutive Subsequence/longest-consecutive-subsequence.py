class Solution:
    def longestConsecutive(self, a):
        curr_set = set(a)
        res = 0
        
        for e in a:
            curr_len = 0
            
            while e in curr_set:
                curr_len += 1
                e -= 1
                
            res = max(res, curr_len)
            
        return res