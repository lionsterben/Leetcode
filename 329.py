class Solution:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        row, col = len(matrix), len(matrix[0])
        dp = [[0]*col for _ in range(row)]
        
        def dfs(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1+max(
                    dfs(i-1, j) if i>0 and val<matrix[i-1][j] else 0,
                    dfs(i, j-1) if j>0 and val<matrix[i][j-1] else 0,
                    dfs(i+1, j) if i<row-1 and val<matrix[i+1][j] else 0,
                    dfs(i, j+1) if j<col-1 and val<matrix[i][j+1] else 0)
            return dp[i][j]
        
        return max(dfs(i, j) for i in range(row) for j in range(col))