class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        p = [0 for _ in primes]
        res = [1]
        while len(res) < n:
            for idx in range(len(primes)):
                while res[p[idx]]*primes[idx] <= res[-1]:
                    p[idx] += 1
            res.append(min([res[p[idx]]*primes[idx] for idx in range(len(p))]))
        return res[-1]
## TLE

from heapq import heappush, heappop
class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        heap = []
        res = [1]
        for i in primes:
            heappush(heap, (i,i,0)) ## val, prime, idx
        while len(res) < n:
            val, prime, idx = heappop(heap)
            if val <= res[-1]:
                while val <= res[-1]:
                    idx += 1
                    val = res[idx]*prime
            else:
                res.append(val)
                val = prime*res[idx+1]
                idx += 1
                
            heappush(heap, (val, prime, idx))
        return res[-1]
## 涉及大数组大小排列，考虑使用堆