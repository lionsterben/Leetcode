class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        while True:
            a = nums[0]
            print(a)
            min_num = []
            max_num = []
            for num in nums[1:]:
                if num <= a:
                    min_num.append(num)
                else:
                    max_num.append(num)
            ind = len(max_num)+1
            if k == ind:
                return a
            elif ind < k:
                k = k-ind
                nums = min_num
            else:
                nums = max_num

from heapq import *
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = [-num for num in nums]
        heapify(nums)
        for i in range(k-1):
            heappop(nums)
        return -heappop(nums)