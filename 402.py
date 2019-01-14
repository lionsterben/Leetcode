class Solution:
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        st = 0
        if k == len(num):
            return "0"
        while st < len(num):
            digit = int(num[st])
            while k>0 and stack and digit < stack[-1]:
                stack.pop()
                # stack.append(digit)
                # print(k)
                k = k-1
            
            # if not stack:
            stack.append(digit)
            st += 1
        print(stack)
        while k > 0:
            stack.pop()
            k = k-1
        print(stack)
        dele_zero = []
        flag = 1
        for i in stack:
            if flag and i == 0:
                continue
            else:
                flag = 0
                dele_zero.append(i)
        print(k)
#         while k > 0:
#             dele_zero.pop()
#             k = k-1
                
        return "".join(map(str,dele_zero)) if "".join(map(str,dele_zero)) else "0"
        
                
        