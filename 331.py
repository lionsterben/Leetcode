class Solution:
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        node = preorder.split(",")
        mem = {}
        # def valid(order):
        #     isnum, notnum = 0, 0
        #     for i in order:
        #         if i == "#":
        #             notnum += 1
        #         else:
        #             isnum += 1
        #     return notnum == isnum+1
        
        def isTree(pre):
            # print(pre)
            if not pre:
                return False
            if len(pre) == 1 and pre[0] == '#':
                return True
            if pre[0] == "#":
                return False
            root = pre[0]
            other = pre[1:]
            # res = []
            isnum, notnum = 0, 0
            for i in other:
                if i == "#":
                    notnum += 1
                else:
                    isnum += 1
            if isnum+2 != notnum:
                return False
            left_num, left_nonum = 0, 0
            for i in range(len(other)-1):
                cur = other[i]
                if cur == "#":
                    left_nonum += 1
                else:
                    left_num += 1
                if left_nonum == left_num+1:
                    left = other[:i+1]
                    right = other[i+1:]
                    if tuple(left) in mem:
                        cc_left = mem[tuple(left)]
                    else:
                        cc_left = isTree(left)
                    if tuple(right) in mem:
                        cc_right = mem[tuple(right)]
                    else:
                        cc_right = isTree(right)
                    if cc_left and cc_right:
                        mem[tuple(pre)] = True
                        return True
                    # res.append(isTree[left] and isTree[right])
            mem[tuple(pre)] = False
            return False
            # if not res
            
        cc = isTree(node)     
        # print(mem)
        return cc
## TLE 148/150

class Solution:
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        p = preorder.split(',')
        stack = []
        for i in p:
            stack.append(i)
            while len(stack) > 1 and stack[-1] == "#" and stack[-2] == "#":
                stack.pop()
                stack.pop()
                if not stack:
                    return False
                stack[-1] = "#"
                
        return stack == ['#']

## use stack