import math
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = {}
        def num(n):
            if int(math.sqrt(n)) == math.sqrt(n):
                dp[n] = 1
                return 1
            res = n
            for i in range(1,n//2+1):
                if int(math.sqrt(i)) == math.sqrt(i):
                    if n-i in dp:
                        c = dp[n-i]
                    else:
                        c = num(n-i)
                        dp[n-i] = c
                    res = min(res, c+1)
            dp[n] = res
            return res
        num(n)
        return dp[n]

class Solution:
    temp = [0,1,2,3]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 4:
            return self.temp[n]
        for i in range(len(self.temp), n+1):
            res = n
            j = 1
            while (i-j*j) >= 0:
                res = min(res, self.temp[i-j*j]+1)
                j += 1
            self.temp += [res]
        return self.temp[n]

#BFS
def numSquares(self, n):
    if n < 2:
        return n
    lst = []
    i = 1
    while i * i <= n:
        lst.append( i * i )
        i += 1
    cnt = 0
    toCheck = {n}
    while toCheck:
        cnt += 1
        temp = set()
        for x in toCheck:
            for y in lst:
                if x == y:
                    return cnt
                if x < y:
                    break
                temp.add(x-y)
        toCheck = temp

    return cnt