class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = {}
        for row in range(len(triangle)):
            for idx in range(len(triangle[row])):
                if row == 0:
                    dp[(0,0)] = triangle[row][idx]
                    continue
                cc = 1<<20
                if (row-1, idx-1) in dp:
                    cc = min(cc, dp[(row-1, idx-1)])
                if (row-1, idx) in dp:
                    cc = min(cc, dp[(row-1, idx)])
                dp[(row, idx)] = cc+triangle[row][idx]
        res = 1<<20
        # print(dp)
        for idx in range(len(triangle[-1])):
            if dp[(len(triangle)-1,idx)] < res:
                res = dp[(len(triangle)-1,idx)]
        return res

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]