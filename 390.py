class Solution:
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        remain = n
        head = 1
        from_left = True
        step = 1
        while remain > 1:
            if from_left or remain%2 == 1:
                head += step
            step *= 2
            remain = remain // 2
            from_left = not from_left
            
        return head
        
                    
##直接标记，从左到右，head一定加一，从右往左，如果remain是奇数，也加一，每一步remain都减少一半