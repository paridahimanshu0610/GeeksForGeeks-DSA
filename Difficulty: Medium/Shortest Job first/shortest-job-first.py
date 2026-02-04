#User function Template for python3
from math import floor
class Solution:
    def solve(self, bt):
        bt.sort()
        res = 0
        prev_sum = 0
        total_waiting_time = 0
        
        for e in bt:
            curr_waiting_time = prev_sum
            total_waiting_time += curr_waiting_time
            prev_sum += e
        
        return floor(total_waiting_time/len(bt))