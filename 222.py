# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def get_depth(self, node):
        if not node:
            return 0
        else:
            return 1 + self.get_depth(node.left)
    
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        dep = self.get_depth(root)
        right = self.get_depth(root.right)
        if right + 1 == dep:
            return (1 << (dep-1)) + self.countNodes(root.right)
        else:
            return (1<<(dep-2)) + self.countNodes(root.left)

##非常聪明的解法，判断右子树的高度，如果和root只差一表示左子树是满的，只需要计算右子树的大小；不是的话，表明右子树是比root少一层的满二叉树，这时候只需要计算左子树，递归解决