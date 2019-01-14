class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) <= 1:
            return 0
        class TrieNode:
            def __init__(self, isend=False, val=0):
                self.child = [None for _ in range(2)]
                self.val = val
                self.isend = isend
        
        def num2binary(num):
            res = []
            while num > 0:
                res.append(num%2)
                num = num //2
            res = list(reversed(res))
            res = [0]*(32-len(res)) + res
            return res
        
        root = TrieNode()
        for num in nums:
            node = root
            binary = num2binary(num)
            for idx, bit in enumerate(binary):
                if idx == len(binary)-1:
                    node.child[bit] = TrieNode(True, num)
                else:
                    if node.child[bit] is None:
                        node.child[bit] = TrieNode()
                node = node.child[bit]
        
        while root.child[0] is None or root.child[1] is None:
            if root.child[0] is not None:
                root = root.child[0]
            else:
                root = root.child[1]
        left, right = root.child[0], root.child[1]
        
        def maxhelper(node_left, node_right):
            if node_left.isend and node_right.isend:
                return node_left.val ^ node_right.val
            if node_right.child[0] is None:
                return maxhelper(node_left.child[0] if node_left.child[0] else node_left.child[1], node_right.child[1])
            elif node_right.child[1] is None:
                return maxhelper(node_left.child[1] if node_left.child[1] else node_left.child[0], node_right.child[0])
            elif node_left.child[0] is None:
                return maxhelper(node_left.child[1], node_right.child[0])
            elif node_left.child[1] is None:
                return maxhelper(node_left.child[0], node_right.child[1])
            else:
                return max(maxhelper(node_left.child[1], node_right.child[0]), maxhelper(node_left.child[0], node_right.child[1]))
        return maxhelper(left, right)

##寻找数组中最大的异或值，高位首先比较，尽量变成0，1或者1，0