class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        def _combine(start, tmp_k, tmp):
            if tmp_k == 0:
                res.append(tmp[:])
                return
            else:
                # trick: end search early, only for enough number
                for i in range(start, n - tmp_k + 2):
                    print(i)
                    tmp.append(i)
                    # print(tmp)
                    _combine(i + 1, tmp_k - 1, tmp)
                    tmp.pop()
        _combine(1, k, [])
        return res