#User function Template for python3

class Solution:
    def countPrimes(self, l, r):
        prime_status = [1]*r
        prime_status[0] = 0
        
        for i in range(2, math.ceil(math.sqrt(r+1))):
            if prime_status[i-1]==1:
                # print(i)
                for j in range(i*i, r+1, i):
                    prime_status[j-1] = 0
        
        # print(prime_status)
        return sum(prime_status[l-1:])