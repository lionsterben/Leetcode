class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #先寻找旋转点
        i, j = 0, len(nums)-1
        rotate = -1
        while i <= j:
            middle = (i+j)//2
            if middle != 0:
                if nums[middle] < nums[middle-1]:
                    rotate = middle
                    break
            else:
                if len(nums) == 1:
                    break
                if nums[middle + 1] < nums[middle]:
                    rotate = middle + 1
                    break
            if nums[middle] > nums[0]:
                i = middle + 1
            else:
                j = middle - 1
        def binary_search(nums, target):
            i, j = 0, len(nums)-1
            while i <= j:
                middle = (i+j)//2
                if nums[middle] == target:
                    return middle
                if nums[middle] > target:
                    j = middle - 1
                if nums[middle] < target:
                    i = middle + 1
            return -1
        print(rotate)
        if rotate != -1:
            a1 = binary_search(nums[:rotate], target)
            a2 = binary_search(nums[rotate:], target)
        else:
            return binary_search(nums, target)
        if a1 != -1:
            return a1
        if a2 != -1:
            return a2 + rotate   
        else:
            return -1