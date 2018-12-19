class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1 or len(nums) == 2:
            return max(nums)
        def with_mask(nums):
            dp = [(nums[0], 1)]
            if nums[1] < nums[0]:
                dp.append((nums[0], 1))
            else:
                dp.append((nums[1], 0))
            for i in range(2, len(nums)-1):
                if dp[i-2][0]+nums[i] > dp[i-1][0]:
                    dp.append((dp[i-2][0]+nums[i], dp[i-2][1]))
                elif dp[i-2][0]+nums[i] < dp[i-1][0]:
                    dp.append((dp[i-1][0], dp[i-1][1]))
                else:
                    if dp[i-1][0] and dp[i-2][0]:
                        dp.append((dp[i-1][0], 1))
                    else:
                        dp.append((dp[i-1][0], 0))
            if dp[len(nums)-3][1] == 1:
                return max(dp[len(nums)-2][0], nums[-1])
            else:
                return max(dp[len(nums)-3][0]+nums[-1], dp[len(nums)-2][0])
        def getta(nums):
            dp = [nums[0]]
        #         if nums[1] < nums[0]:
        #             dp.append((nums[0], 1))
        #         else:
        #             dp.append((nums[1], 0))
            dp.append(max(nums[0], nums[1]))
            for i in range(2, len(nums)):
                if dp[i-2]+nums[i] > dp[i-1]:
                    dp.append(dp[i-2]+nums[i])
                else:
                    dp.append(dp[i-1])
            return dp[-1]
        return max(with_mask(nums), getta(nums[1:]))

        ## my solution , so ugly

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums)
        
        # case1: rob nums[0] --- [0, n-1]
        pre2 = pre1 = nums[0]
        for i in range(2, len(nums)-1):
            cur = max(pre2 + nums[i], pre1)  
            pre2, pre1 = pre1, cur
        temp = pre1
        
        # case2: not rob nums[0] --- [1, n]
        pre2 = pre1 = 0
        for i in range(1, len(nums)):
            cur = max(pre2 + nums[i], pre1)
            pre2, pre1 = pre1, cur
        
        return max(temp, pre1)