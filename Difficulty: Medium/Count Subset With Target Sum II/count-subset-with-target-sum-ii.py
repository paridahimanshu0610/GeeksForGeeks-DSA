from collections import defaultdict

class Solution:
    # Recursive function to generate all subset sums
    def genSubset(self, arr, index, currSum, freq):
        if index == len(arr):
            # store frequency of currSum
            freq[currSum] += 1
            return
    
        # Include current element
        self.genSubset(arr, index + 1, currSum + arr[index], freq)
    
        # Skip current element
        self.genSubset(arr, index + 1, currSum, freq)
    
    # Function to count subsets whose sum equals k using frequency maps
    def countSubset(self, arr, k):
        n = len(arr)
        mid = n // 2
    
        # Split array into two halves
        left = arr[:mid]
        right = arr[mid:]
    
        # Store frequency of all subset sums
        freqLeft = defaultdict(int)
        freqRight = defaultdict(int)
        self.genSubset(left, 0, 0, freqLeft)
        self.genSubset(right, 0, 0, freqRight)
    
        count = 0
    
        # Multiply frequencies of pairs that sum to k
        for sumLeft, fLeft in freqLeft.items():
            target = k - sumLeft
            if target in freqRight:
                count += fLeft * freqRight[target]
    
        return count