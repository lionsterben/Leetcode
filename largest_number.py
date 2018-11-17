class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        comp = lambda a,b:1 if a+b<b+a else -1 if a+b>b+a else 0
        nums = map(str, nums)
        nums.sort(cmp=comp)
        return str(int("".join(nums)))