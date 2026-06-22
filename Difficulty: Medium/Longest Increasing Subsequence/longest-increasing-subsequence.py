class Solution:
    def upNext(self, a, idx, prev_idx, dp):
        if idx == len(a):
            if (prev_idx==0) or (a[idx] > a[prev_idx-1]):
                dp[len(a)-1][prev_idx] = 1
            else:
                dp[len(a)-1][prev_idx] = 0
            
            return dp[len(a)-1][prev_idx]
        
        if dp[idx][prev_idx]:
            return dp[idx][prev_idx]
        
        notTake = self.upNext(a, idx+1, prev_idx, dp)
        
        take = 0
        if (prev_idx==0) or (a[idx] > a[prev_idx-1]):
            take = 1 + self.upNext(a, idx+1, idx+1, dp)
        
        dp[idx][prev_idx] = max(take, notTake)
        
        return dp[idx][prev_idx]
        
    def lis(self, a):
        n = len(a)
        dp = [None]*(n)
        res = 1
        j = 0
        
        dp[j] = a[0]
        j += 1
        
        for i in range(1, n):
            if a[i] > dp[j-1]:
                dp[j] = a[i]
                j += 1
            else:
                l, h = 0, j-1
                pos = j
                while l <= h:
                    mid = l + (h-l)//2
                    if a[i] > dp[mid]:
                        l = mid+1
                    elif a[i] < dp[mid]:
                        pos = min(mid, pos)
                        h = mid-1
                    else:
                        pos = mid
                        break
                dp[pos] = a[i]
                j = j+1 if pos == j else j
                
                # print(i, a[i], dp)
         
        # print(dp)
        
        return j