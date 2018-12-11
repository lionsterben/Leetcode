class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            dp[i][n-1] = 1
        for i in range(n):
            dp[m-1][i] = 1
        for i in reversed(range(m-1)):
            for j in reversed(range(n-1)):
                dp[i][j] = dp[i+1][j]+dp[i][j+1]
        return dp[0][0]