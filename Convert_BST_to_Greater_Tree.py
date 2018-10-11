# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        key = []
        def dfs(head):
            if head == None:
                return
            key.append(head.val)
            dfs(head.left)
            dfs(head.right)
        dfs(root)
        sortKey = sorted(key, reverse = True)
        unique = sorted(list(set(sortKey)), reverse = True)
        num_count = {}
        haha = {}
        count = 0
        for i in sortKey:
            if i not in num_count:
                num_count[i] = 1
            else:
                num_count[i] += 1
        for i in unique:
            haha[i] = i + count
            count += i * num_count[i]
        #print(sortKey)
        # print(root.val)
        def dfs_change(head):
            if head == None:
                return
            head.val = haha[head.val]
            dfs_change(head.left)
            dfs_change(head.right)
        dfs_change(root)
        return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    cursum = 0
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return
        self.convertBST(root.right)
        self.cursum += root.val
        root.val = self.cursum
        self.convertBST(root.left)
        return root