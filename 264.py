class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1]
        p2, p3, p5 = 0, 0, 0
        while len(res) < n:
            while res[p2]*2 <= res[-1]:
                p2 += 1
            while res[p3]*3 <= res[-1]:
                p3 += 1
            while res[p5]*5 <= res[-1]:
                p5 += 1
            res.append(min(res[p2]*2, res[p3]*3, res[p5]*5))
        # print(res)
        return res[-1]