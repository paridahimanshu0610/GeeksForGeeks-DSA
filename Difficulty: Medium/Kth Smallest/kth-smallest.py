import heapq as hq

class Solution:
    def kthSmallest(self, a, k):
        temp = []

        for i in range(k):
            hq.heappush(temp, -a[i])

        for i in range(k, len(a)):
            if (a[i]) < -temp[0]:
                hq.heappop(temp)
                hq.heappush(temp, -a[i])

        return -temp[0]
