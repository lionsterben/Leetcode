class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.dp = {}
        self.matrix = matrix
        if matrix:
            row, col = len(matrix), len(matrix[0])
            for i in range(row):
                for j in range(col):
                    self.dp[(i,j)] = self.dp.get((i-1,j),0) + self.dp.get((i,j-1),0) - self.dp.get((i-1,j-1),0) + self.matrix[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.dp[(row2,col2)] + self.dp.get((row1-1,col1-1),0) - self.dp.get((row2,col1-1),0) - self.dp.get((row1-1, col2),0)

## 首先计算每个到（0，0）点的sum，再根据这个sum计算其他region的大小，有效降低复杂度