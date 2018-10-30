class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def swap(a, i):
            j = len(nums)-1
            while j > i:
                if nums[j] > nums[i]:
                    nums[j], nums[i] = nums[i], nums[j]
                    break
                j -= 1
        def reverse(a, i):
            st, end = i, len(nums)-1
            while st < end:
                nums[st], nums[end] = nums[end], nums[st]
                st += 1
                end -= 1
        
        ind = len(nums)-1
        while ind > 0:
            if nums[ind] > nums[ind-1]:
                break
            ind -= 1
        if ind == 0:
            reverse(nums,0)
        else:
            swap(nums, ind-1)
            reverse(nums, ind)