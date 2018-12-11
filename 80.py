class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        st, cnt, dup = 0,0,0
        while st+dup < len(nums):
            # print(st, dup, cnt, nums)
            if st == 0:
                cnt = 1
                past = nums[st]
                st += 1
            else:
                if nums[st] == past:
                    cnt += 1
                    if cnt == 3:
                        dup += 1
                        for i in range(st, len(nums)-dup):
                            nums[i], nums[i+1] = nums[i+1], nums[i]
                        cnt -= 1
                    else:
                        st += 1
                else:
                    past = nums[st]
                    st += 1
                    cnt = 1
        return len(nums)-dup

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for num in nums:
            if i < 2 or num > nums[i-2]:
                nums[i] = num
                i += 1
        return i