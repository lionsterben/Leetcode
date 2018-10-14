class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []
        if not nums:
            return 0
        for i in range(len(nums)):
            res = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    res = max(res, dp[j]+1)
            dp.append(res)
        # print(dp)
        return max(dp)
//todo nlogn