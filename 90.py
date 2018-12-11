class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        nums.sort()
        for idx in range(len(nums)):
            if idx == 0 or nums[idx] != nums[idx-1]:
                l = len(res)
            for i in range(len(res)-l, len(res)):
                res.append(res[i]+[nums[idx]])
        return res