class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #dp[ind] = (chose,val)
        #chose:neural:0 cooldown:1 sell:2
        hold, notHold, notHoldCooldown = float('-inf'), 0, float('-inf')
        for price in prices:
            hold = max(notHold-price, hold)
            notHold = max(notHoldCooldown, notHold)
            notHoldCooldown = hold+price
        return max(hold, notHold, notHoldCooldown)

The key is 3 states and 5 edges for state transition. 3 states are notHold (stock), hold (stock), and notHold_cooldown. The initial values of the latter two are negative infinity since they are meaningless, i.e. you won't hold stocks at first and there's no cooldown at first. The 5 edges:

hold -----do nothing----->hold

hold -----sell----->notHold_cooldown

notHold -----do nothing -----> notHold

notHold -----buy-----> hold

notHold_cooldown -----do nothing----->notHold