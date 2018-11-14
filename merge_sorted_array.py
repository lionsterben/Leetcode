class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i, j = m-1, n-1
        ind = len(nums1)-1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[ind] = nums1[i]
                i -= 1
            else:
                nums1[ind] = nums2[j]
                j -= 1
            ind -= 1
        while j >= 0:
            nums1[ind] = nums2[j]
            j -= 1
            ind -= 1
                
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        res = []
        i, j = 0, 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        if i != m:
            res.extend(nums1[i:])
        if j != n:
            res.extend(nums2[j:])
        for i in range(len(nums1)):
            nums1[i] = res[i]     