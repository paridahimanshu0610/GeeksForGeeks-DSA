import heapq

class Solution:
    def minSteps(self, a, start, end):
        n = len(a)
        minDist = [float("inf")]*1000
        minHeap = []
        
        heapq.heappush(minHeap, (0,0,start%1000))
        minDist[start%1000] = 0
        
        while len(minHeap)!=0:
            currSteps,currNode,prodSoFar = heapq.heappop(minHeap)
            
            if currSteps > minDist[prodSoFar]:
                continue
            
            for nv in range(n+1):
                if nv == 0:
                    continue
                
                tempProd = (prodSoFar*a[nv-1])%1000
                tempSteps = currSteps+1
                
                if tempSteps < minDist[tempProd]:
                    minDist[tempProd] = tempSteps
                    heapq.heappush(minHeap, (tempSteps,nv,tempProd))
                    
        return -1 if minDist[end%1000]==float("inf") else minDist[end%1000]  