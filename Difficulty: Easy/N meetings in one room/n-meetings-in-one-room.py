class Solution:
    def maximumMeetings(self, start, end):
        meetings = [interval for interval in zip(start, end)]
        meetings.sort(key=lambda x: x[1])
        
        curr_start, curr_end = -1, -1
        res = 0
        
        for i in range(len(meetings)):
            temp_start, temp_end = meetings[i]
            
            if temp_start > curr_end:
                curr_start, curr_end = temp_start, temp_end
                res += 1
        
        return res