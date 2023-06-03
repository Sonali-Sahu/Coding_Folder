# Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)
        
        dp = [[0 for i in range(len(s1) + 1)] for j in range(len(s2) + 1)]

        for i in range(len(s2) + 1):
            for j in range(len(s1) + 1):
                if i == 0 and j == 0: 
                    continue
                elif i == 0:
                    dp[i][j] += dp[i][j-1] + ord(s1[j-1])
                elif j  == 0:
                    dp[i][j] += dp[i-1][j] + ord(s2[i-1])
                elif s1[j-1] == s2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(ord(s1[j-1]) + dp[i][j-1], ord(s2[i-1]) + dp[i-1][j])
        
        return dp[n][m]
