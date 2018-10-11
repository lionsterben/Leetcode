class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        min_num, max_num = nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                min_num, max_num = max_num, min_num
            min_num = min(min_num*nums[i], nums[i])
            max_num = max(max_num*nums[i], nums[i])
            res = max(res, max_num)
        return res
动态规划依赖两个状态