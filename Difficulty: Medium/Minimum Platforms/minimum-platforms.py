class Solution:
    def findStation(self, last_train_depart_time, start_time):
        idle_time = float('inf')
        res = None
        
        for i, depart_time in enumerate(last_train_depart_time):
            if start_time > depart_time:
                temp = start_time-depart_time
                if temp < idle_time:
                    res = i
                    idle_time = temp
                        
        return res
        
    def minPlatform(self, arr, dep):
        arr.sort()
        dep.sort()
        i, j = 0, 0
        n = len(arr)
        cnt, max_cnt = 0, 0 
        
        while i < n and j < n:
            if arr[i] <= dep[j]:
                cnt += 1
                max_cnt = max(cnt, max_cnt)
                i += 1
            else:
                cnt -= 1
                j += 1
        
        return max_cnt