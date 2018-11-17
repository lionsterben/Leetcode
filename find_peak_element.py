class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def search(left, right):
            if left == right:
                return left
            mid = (left + right) // 2
            if nums[mid] > nums[mid+1]:
                return search(left, mid)
            else:
                return search(mid+1, right)
        return search(0, len(nums)-1)