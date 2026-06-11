class Solution:
    def getAllSeq(self, s1, s2, idx1, idx2, soFarStr, res, seqLen, dp):
        if len(soFarStr) == seqLen:
            res.append("".join(soFarStr))
            return

        for char_idx in range(ord('a'), ord('z')+1):
            found = False
            for i in range(idx1, len(s1)):
                if s1[i] == chr(char_idx):
                    for j in range(idx2, len(s2)):
                        if (s1[i] == s2[j]) and (dp[i+1][j+1] == len(soFarStr) + 1):
                            soFarStr.append(s1[i])
                            self.getAllSeq(s1, s2, i+1, j+1, soFarStr, res, seqLen, dp)
                            soFarStr.pop()
                            found = True
                            break

                    if found:
                        break

	def allLCS(self, s1, s2):
	    m, n = len(s1), len(s2)
	    dp = [[0]*(n+1) for _ in range(m+1)]

	    for idx1 in range(1, m+1):
	        for idx2 in range(1, n+1):
	            if s1[idx1-1] == s2[idx2-1]:
	                dp[idx1][idx2] = 1 + dp[idx1-1][idx2-1]
	            else:
	                dp[idx1][idx2] = max(dp[idx1][idx2-1], dp[idx1-1][idx2])

	    seqLen = dp[m][n]
	    res = []

	    self.getAllSeq(s1, s2, 0, 0, [], res, seqLen, dp)

	    return res
