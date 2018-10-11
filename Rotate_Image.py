class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row, height = len(matrix), len(matrix[0])
        for i in range(row//2):
            for j in range(height):
                matrix[i][j], matrix[row-i-1][j] = matrix[row-i-1][j], matrix[i][j]
        print(matrix)
        for i in range(row):
            for j in range(i+1, height):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]