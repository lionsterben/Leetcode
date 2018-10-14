class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def search(a, target):
            i, j = 0, len(a)-1
            while i <= j:
                ind = (i+j)//2
                if a[ind] == target:
                    return (True,ind)
                if a[ind] < target:
                    i = ind+1
                if a[ind] > target:
                    j = ind-1
            return (False,i)
        if len(matrix) == 0:
            return False
        row_i, row_j, col_i, col_j = 0, len(matrix)-1, 0, len(matrix[0])-1
        while row_i <= row_j and col_i <= col_j:
            row = [matrix[i][col_i] for i in range(row_i, row_j+1)]
            col = [matrix[row_i][i] for i in range(col_i, col_j+1)]
            row_res = search(row, target)
            col_res = search(col, target)
            if row_res[0] or col_res[0]:
                return True
            row_j = row_res[1]+row_i-1
            col_j = col_res[1]+col_i-1
            row_i += 1
            col_i += 1
        return False

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        x, y = 0, len(matrix[0])-1
        while x < len(matrix) and y >= 0:
            if matrix[x][y] < target:
                x += 1
            elif matrix[x][y] > target:
                y -= 1
            else:
                return True
        return False