class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = {}
        def cal(nums):
            if len(nums) == 1:
                return nums[0]
            maxCnt = 0
            for i in range(len(nums)):
                tmp = 0
                if i == 0:
                    tmp += nums[0]*nums[1]
                elif i == len(nums)-1:
                    tmp += nums[-1]*nums[-2]
                else:
                    tmp += nums[i]*nums[i-1]*nums[i+1]
                cc = nums.copy()
                cc.pop(i)
                if tuple(cc) in dp:
                    tmp += dp[tuple(cc)]
                else:
                    hehe = cal(cc)
                    dp[tuple(cc)] = hehe
                    tmp += hehe
                # tmp += cal(cc)
                maxCnt = max(maxCnt, tmp)
            return maxCnt
        return cal(nums)
                    
            
class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        coin = [1] + [num for num in nums if num > 0] + [1]
        n = len(coin)
        dp = [[0] * n for _ in range(n)]
        for k in range(2, n):
            for left in range(0,n-k):
                right = left + k
                for i in range(left+1, right):
                    dp[left][right] = max(dp[left][right], coin[i]*coin[left]*coin[right]+dp[left][i]+dp[i][right])
        return dp[0][n-1]
                    
            
            