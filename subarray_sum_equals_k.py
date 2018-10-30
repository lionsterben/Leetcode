class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dp = {}
        def privateSub(ind, k):
            if ind == len(nums):
                return 0
            if k == nums[ind]:
                if (ind+1, 0) in dp:
                    return 1 + dp[(ind+1, 0)]
                else:
                    cc = privateSub(ind+1, 0)
                    dp[(ind+1, 0)] = cc
                    return 1 + cc
            if (ind+1, k-nums[ind]) in dp:
                return dp[(ind+1, k-nums[ind])]
            else:
                m = privateSub(ind+1, k-nums[ind])
                dp[(ind+1, k-nums[ind])] = m
                return m
        cnt = 0
        for i in range(len(nums)):
            cnt += privateSub(i,k)
        return cnt

class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        persum = {}
        cnt = 0
        res = 0
        persum[0] = 1
        for num in nums:
            cnt += num
            if cnt - k in persum:
                res += persum[cnt-k]
            persum[cnt] = persum.get(cnt,0)+1
        return res
           