class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lt, i, gt = 0, 0, len(nums)-1
        while i <= gt:
            if nums[i] < 1:
                nums[lt], nums[i] = nums[i], nums[lt]
                lt += 1
                i += 1
            elif nums[i] > 1:
                nums[i], nums[gt] = nums[gt], nums[i]
                gt -= 1
            else:
                i += 1