class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return True
        cc = sum(nums)
        if cc % 2 == 1:
            return False
        target = int(cc/2)
        dp = [False for _ in range(target+1)]
        dp[0] = True
        for num in nums:
            for j in reversed(range(num, target+1)):
                dp[j] = dp[j] or dp[j-num]
        # print(dp)
        return dp[target]

dp背包问题