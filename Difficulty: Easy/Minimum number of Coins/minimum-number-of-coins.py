class Solution:
    def findMin(self, n):
        cnt = 0
        curr = n
       
        while curr > 0:
            if curr >= 10:
                temp = curr//10
                curr -= 10*temp
                cnt += temp
            elif curr >= 5:
                curr -= 5
                cnt += 1
            elif curr >= 2:
                temp = curr//2
                curr -= 2*temp
                cnt += temp
            else:
                curr -= 1
                cnt += 1
            
        return cnt