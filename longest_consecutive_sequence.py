class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        maxSum = -1
        if not nums:
            return 0
        for num in nums:
            if num-1 not in nums:
                cnt = 1
                while num + 1 in nums:
                    cnt += 1
                    num = num + 1
                if cnt > maxSum:
                    maxSum = cnt
        return maxSum