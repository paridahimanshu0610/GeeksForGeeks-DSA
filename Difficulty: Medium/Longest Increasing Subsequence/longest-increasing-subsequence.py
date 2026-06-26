class Solution:
    def upNext(self, a, curr_idx, prev_idx, dp):
        if curr_idx == len(a)-1:
            if (prev_idx==0) or (a[curr_idx] > a[prev_idx-1]):
                dp[curr_idx][prev_idx] = 1
            else:
                dp[curr_idx][prev_idx] = 0

            return dp[curr_idx][prev_idx]

        if dp[curr_idx][prev_idx] is not None:
            return dp[curr_idx][prev_idx]

        notPick = self.upNext(a, curr_idx+1, prev_idx, dp)
        
        pick = 0
        if (prev_idx==0) or (a[curr_idx] > a[prev_idx-1]):
            pick = 1 + self.upNext(a, curr_idx + 1, curr_idx+1, dp)

        dp[curr_idx][prev_idx] = max(pick, notPick)

        return dp[curr_idx][prev_idx]
    
    def get_pos_to_replace(self, temp, x):
        n = len(temp)
        l, h = 0, n-1
        
        while l <= h:
            mid = (l+h)//2
            if temp[mid] == x:
                return mid
            elif x > temp[mid]:
                l = mid+1
            else:
                h = mid-1
            
        return l
        
    def lis(self, a):
        n = len(a)
        temp = [a[0]]
        
        for i in range(1, n):
            if a[i] > temp[-1]:
                temp.append(a[i])
            else:
                # print(i, a[i], temp, sep = " | ")
                pos = self.get_pos_to_replace(temp, a[i])
                # print(pos)
                if pos < len(temp):
                    temp[pos] = a[i]
                else:
                    temp.append(a[i])
            
        return len(temp)