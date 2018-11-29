class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0 for _ in nums]
        def sort(enums):
            half = len(enums)//2
            if half:
                left, right = sort(enums[:half]), sort(enums[half:])
                for i in reversed(range(len(enums))):
                    if not right or (left and left[-1][1]>right[-1][1]):
                        res[left[-1][0]] += len(right)
                        enums[i] = left.pop()
                    else:
                        enums[i] = right.pop()
            return enums
        enums = list(enumerate(nums))
        sort(enums)
        return res