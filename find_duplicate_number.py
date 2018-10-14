class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 1, len(nums)-1
        while low < high:
            mid = (low+high)//2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count <= mid:
                low = mid+1
            else:
                high = mid
        return low