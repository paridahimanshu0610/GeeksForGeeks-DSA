class Solution:
    def soFar(self, s1, s2, idx1, idx2, dp):
        if idx1 < 0 or idx2 < 0:
            return 0
        
        if dp[idx1][idx2] is not None:
            return dp[idx1][idx2]
        
        if s1[idx1] == s2[idx2]:
            dp[idx1][idx2] = 1 + self.soFar(s1, s2, idx1-1, idx2-1, dp)
        else:
            dp[idx1][idx2] = max(self.soFar(s1, s2, idx1, idx2-1, dp), self.soFar(s1, s2, idx1-1, idx2, dp))
            
        return dp[idx1][idx2]
    
    def getAllLCS(self, s1, s2, idx1, idx2, soFarLCS, all_lcs, leftOut, dp, maxLen):
        if leftOut == 0:
            all_lcs.append("".join(soFarLCS))
            return

        currLCS = maxLen - leftOut

        for ch in range(ord('a'), ord('z') + 1):
            done = False
            for i in range(idx1, len(s1)):
                if s1[i] == chr(ch):
                    for j in range(idx2, len(s2)):
                        if s2[j] == chr(ch) and dp[i][j] == currLCS+1:
                            soFarLCS.append(s1[i])
                            self.getAllLCS(s1, s2, i+1, j+1, soFarLCS, all_lcs, leftOut-1, dp, maxLen)
                            soFarLCS.pop()
                            done = True
                            break
                if done:
                    break
	
	def allLCS(self, s1, s2):
	    m, n = len(s1), len(s2)
	    dp = [[None]*n for _ in range(m)]
	    
	    self.soFar(s1, s2, m-1, n-1, dp)
	    maxLen = dp[m-1][n-1]
	    
	    res = []
	    self.getAllLCS(s1, s2, 0, 0, [], res, maxLen, dp, maxLen)
	    
	    return res