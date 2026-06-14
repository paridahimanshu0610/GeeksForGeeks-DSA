class Solution:
	def minDifference(self, arr):
	    n = len(arr)
        totSum = 0

        # Calculate the total sum of the array
        for i in range(n):
            totSum += arr[i]

        # Initialize a boolean list 'prev' to represent the previous row of the DP table
        prev = [False] * (totSum + 1)

        # Base case: If no elements are selected (sum is 0), it's a valid subset
        prev[0] = True

        # Initialize the first row based on the first element of the array
        if arr[0] <= totSum:
            prev[arr[0]] = True

        # Fill in the DP table using a bottom-up approach
        for ind in range(1, n):
            # Create a boolean list 'cur' to represent the current row of the DP table
            cur = [False] * (totSum + 1)
            cur[0] = True

            for target in range(1, totSum + 1):
                # Exclude the current element
                notTaken = prev[target]

                # Include the current element if it doesn't exceed the target
                taken = False
                if arr[ind] <= target:
                    taken = prev[target - arr[ind]]

                cur[target] = notTaken or taken

            # Set 'cur' as the 'prev' for the next iteration
            prev = cur

        mini = int(1e9)
        for i in range(totSum + 1):
            if prev[i]:
                # Calculate the absolute difference between two subset sums
                diff = abs(i - (totSum - i))
                mini = min(mini, diff)

        return mini